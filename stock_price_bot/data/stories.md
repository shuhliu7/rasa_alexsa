## basic story
* greet
  - utter_whichStock
* inform{"stock":"AAPL"}
  - search_stock_price
  - slot{"stock":"AAPL"}
> check_asked_question

## story no more checks
> check_asked_question
* deny
  - utter_goodbye
## story yes more checks
> check_asked_question
* affirm
  - utter_whichStock
> check_stock_ticker
## keep searching
> check_stock_ticker
* inform{"stock":"AAPL"}
  - search_stock_price
  - slot{"stock":"AAPL"}
> check_asked_question

## company name
* greet
  - utter_whichStock
* inform{"company_name":"APPLE INC"}
  - search_stock_price_company
  - slot{"company_name":"APPLE INC"}
> check_asked_question

## story no more checks
> check_asked_question
* deny
  - utter_goodbye
## story yes more checks
> check_asked_question
* affirm
  - utter_whichStock
> check_stock_ticker
## keep searching
> check_stock_ticker
* inform{"company":"ASBURY AUTOMOTIVE GROUP"}
  - search_stock_price_company
  - slot{"company":"ASBURY AUTOMOTIVE GROUP"}
> check_asked_question

## basic story1
* greet
  - utter_whichStock
* inform{"company_name":"APPLE INC"}
  - search_stock_price_company
  - slot{"company_name":"APPLE INC"}
> check_asked_question

## story no more checks
> check_asked_question
* deny
  - utter_goodbye
## story yes more checks
> check_asked_question
* affirm
  - utter_whichStock
> check_stock_ticker
## keep searching
> check_stock_ticker
* inform{"stock":"AAPL"}
  - search_stock_price
  - slot{"stock":"AAPL"}
> check_asked_question

## basic story2
* greet
  - utter_whichStock
* inform{"stock":"AAPL"}
  - search_stock_price
  - slot{"stock":"AAPL"}
> check_asked_question

## story no more checks
> check_asked_question
* deny
  - utter_goodbye
## story yes more checks
> check_asked_question
* affirm
  - utter_whichStock
> check_stock_ticker
## keep searching
> check_stock_ticker
* inform{"company_name":"APPLE INC"}
  - search_stock_price_company
  - slot{"company_name":"AAPL"}
> check_asked_question
