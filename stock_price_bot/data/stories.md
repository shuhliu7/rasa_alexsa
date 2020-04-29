
<!-- ## path
* greet
  - utter_whichStock
* inform{"stock":'AAPL'}
  - search_stock_price
* goodbye
  - utter_goodbye -->


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
