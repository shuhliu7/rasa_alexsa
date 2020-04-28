
<!-- ## path
* greet
  - utter_whichStock
* inform{"stock":'AAPL'}
  - search_stock_price
* goodbye
  - utter_goodbye -->


## path
* greet
  - utter_whichStock
* inform{"stock":"AAPL"}
  - search_stock_price
  - slot{"stock":"AAPL"}
