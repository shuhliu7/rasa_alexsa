from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from iexfinance.refdata import get_symbols
from iexfinance.stocks import Stock
# from iexfinance.stocks import get_company_name
import numpy as np
import pandas as pd
import json
import os

my_token = "sk_0811f15ee8374e6290f7bf0a5aebc83f"
stock_list = get_symbols(output_format='pandas', token="sk_0811f15ee8374e6290f7bf0a5aebc83f")['symbol'].tolist()
# company_list = get_company_name(output_format='pandas', token="sk_0811f15ee8374e6290f7bf0a5aebc83f")['companyName'].tolist()

def get_stock_price(stock_sticker):
    a = Stock(stock_sticker, token=my_token)
    return a.get_quote()['latestPrice']

#df = pd.read_json("https://api.iextrading.com/1.0/ref-data/symbols")
#df1 = df[['symbol','name']]


script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, './stockTickerCompany.csv')
df2 = pd.read_csv(file_path)
# original list
company_list1 = df2['name'].tolist()
# simpliefied capital list
company_list2=df2['name_no_INC_no_CORP_no_LTD_no_CO_no_ETF_no_Group_no_sa_no_Holdings_no_Ltd'].tolist()
company_list3 = df2['proper shorter'].tolist()
company_list4 = df2['others1'].tolist()
class SearchStockPrice(Action):

    def name(self) -> Text:
        return "search_stock_price"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        stock = tracker.get_slot("stock").upper()

        if stock in stock_list:
            price = get_stock_price(stock)
            dispatcher.utter_message("Here is the price of the stock {}:{}. Would you like to continue?".format(stock, price))

            return [SlotSet("stock", stock)]

        else:
            dispatcher.utter_message("Stock {} does not exist. Would you like to continue?".format(stock))
            return [SlotSet("stock", stock)]

class SearchStockPriceCompany(Action):

    def name(self) -> Text:
        return "search_stock_price_company"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        company_name = tracker.get_slot("company_name")
        c = company_name.upper()

        if c in company_list1:
            stock = df2.loc[df2['name'] == c]['symbol'].values[0]
            if stock in stock_list:
                price = get_stock_price(stock)
                dispatcher.utter_message("Here is the stock price of the company {}:{}. Would you like to continue?".format(company_name, price))
                return [SlotSet("company_name", company_name)]

            else:
                dispatcher.utter_message("Sorry, no result yields for company {}. Would you like to continue?".format(company_name))
                return [SlotSet("company_name", company_name)]

        elif c in company_list2:
            stock = df2.loc[df2['name_no_INC_no_CORP_no_LTD_no_CO_no_ETF_no_Group_no_sa_no_Holdings_no_Ltd']==c]['symbol'].values[0]
            if stock in stock_list:
                price = get_stock_price(stock)
                dispatcher.utter_message("Here is the stock price of the company {}:{}. Would you like to continue?".format(company_name, price))
                return [SlotSet("company_name", company_name)]

            else:
                dispatcher.utter_message("Sorry, no result yields for company {}. Would you like to continue?".format(company_name))
                return [SlotSet("company_name", company_name)]
        elif c in company_list3:
            stock = df2.loc[df2['proper shorter']==c]['symbol'].values[0]
            if stock in stock_list:
                price = get_stock_price(stock)
                dispatcher.utter_message("Here is the stock price of the company {}:{}. Would you like to continue?".format(company_name, price))
                return [SlotSet("company_name", company_name)]

            else:
                dispatcher.utter_message("Sorry, no result yields for company {}. Would you like to continue?".format(company_name))
                return [SlotSet("company_name", company_name)]

        elif c in company_list4:
            stock = df2.loc[df2['others1']==c]['symbol'].values[0]
            if stock in stock_list:
                price = get_stock_price(stock)
                dispatcher.utter_message("Here is the stock price of the company {}:{}. Would you like to continue?".format(company_name, price))
                return [SlotSet("company_name", company_name)]

            else:
                dispatcher.utter_message("Sorry, no result yields for company {}. Would you like to continue?".format(company_name))
                return [SlotSet("company_name", company_name)]
        else:
            dispatcher.utter_message("Sorry, no result yields for company {}. Would you like to continue?".format(company_name))
            return [SlotSet("company_name", company_name)]
