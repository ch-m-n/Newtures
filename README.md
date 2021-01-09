# Newtures
Binance Futures trading bot

Please read comments in `strategy.py` for more information about trading options
Option #1: Scaning all available symbols on Futures Market and place orders when meet conditions
Option #2: Selected symbols only

Note: This is a Heroku bot and use TA-Lib as technical indicators library so you need include TA-Lib buildpack for your Heroku app

`https://elements.heroku.com/buildpacks/numrut/heroku-buildpack-python-talib`

because this library cannot be build through pip alone
