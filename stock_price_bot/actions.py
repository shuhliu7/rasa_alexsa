

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from iexfinance.refdata import get_symbols
from iexfinance.stocks import Stock

my_token = "sk_0811f15ee8374e6290f7bf0a5aebc83f"
def get_stock_price(stock_sticker):
    a = Stock(stock_sticker, token=my_token)
    return a.get_quote()['latestPrice']
"""
class ContinueForm(FormAction):
    # Example of a custom form action

    def name(self):
        # type: () -> Text
        # Unique identifier of the form

        return "continue_form"



   @staticmethod

   def required_slots(tracker):
       # type: () -> List[Text] A list of required slots that the form has to fill

       return ["continue"]

def submit(self, dispatcher, tracker, domain):
    continue  = tracker.get_slot("continue_form")
    If (continue == "Y"):
        continue = True;
    elsif (extracted_value == "N"):
        continue = False;
    return [SlotSet("continue", continue),FollowupAction("utter_whichStock")]"""
class SearchStockPrice(Action):

    def name(self) -> Text:
        return "search_stock_price"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        stock = tracker.get_slot("stock")
        price = get_stock_price(stock)
        dispatcher.utter_message("Here is the price of the {}:{}. Would you like to continue?".format(stock, price))

        return [SlotSet("stock", stock)]
