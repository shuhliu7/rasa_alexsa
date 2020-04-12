## apple path, happy, without price change
* greet
  - utter_greet
* mood_great
  - utter_happy
* check_stock
  - utter_whichStock
* check_apple
  - utter_apple
* affirm
  - utter_sure

## apple path, sad, without price change
* greet
  - utter_greet
* mood_unhappy
  - utter_sad
* check_stock
  - utter_whichStock
* check_apple
  - utter_apple
* affirm
  - utter_sure

## apple path, happy, with price change
  * greet
    - utter_greet
  * mood_great
    - utter_happy
  * check_stock
    - utter_whichStock
  * check_apple
    - utter_apple
  * check_change
    - utter_apple1
  * affirm
    - utter_sure

## apple path, sad, with price change
      * greet
        - utter_greet
      * mood_unhappy
        - utter_sad
      * check_stock
        - utter_whichStock
      * check_apple
        - utter_apple
      * check_change
        - utter_apple1
      * affirm
        - utter_sure


## tesla path, happy, without price change
  * greet
    - utter_greet
  * mood_great
    - utter_happy
  * check_stock
    - utter_whichStock
  * check_tesla
    - utter_tesla
  * affirm
    - utter_sure

## tesla path, unhappy, without price change
      * greet
        - utter_greet
      * mood_unhappy
        - utter_sad
      * check_stock
        - utter_whichStock
      * check_tesla
        - utter_tesla
      * affirm
        - utter_sure

## tesla path, happy, with price change
  * greet
    - utter_greet
  * mood_great
    - utter_happy
  * check_stock
    - utter_whichStock
  * check_tesla
    - utter_tesla
  * check_change
    - utter_tesla1  
  * affirm
    - utter_sure
## tesla path, unhappy, with price change
      * greet
        - utter_greet
      * mood_unhappy
        - utter_sad
      * check_stock
        - utter_whichStock
      * check_tesla
        - utter_tesla
      * check_change
        - utter_tesla1  
      * affirm
        - utter_sure

## SP path, happy, without price change
  * greet
    - utter_greet
  * mood_great
    - utter_happy
  * check_stock
    - utter_whichStock
  * check_S&P500_Index
    - utter_S&P500_Index
  * affirm
    - utter_sure

## SP path, happy, without price change
      * greet
        - utter_greet
      * mood_unhappy
        - utter_sad
      * check_stock
        - utter_whichStock
      * check_S&P500_Index
        - utter_S&P500_Index
      * affirm
        - utter_sure

## SP path, happy, with price change
  * greet
    - utter_greet
  * mood_great
    - utter_happy
  * check_stock
    - utter_whichStock
  * check_S&P500_Index
    - utter_S&P500_Index
  * check_change
    - utter_S&P500_Index1  
  * affirm
    - utter_sure

## SP path, happy, with price change
      * greet
        - utter_greet
      * mood_unhappy
        - utter_sad
      * check_stock
        - utter_whichStock
      * check_S&P500_Index
        - utter_S&P500_Index
      * check_change
        - utter_S&P500_Index1  
      * affirm
        - utter_sure

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
