import Binance
import json
import pandas as pd
import requests
import bot
from talib import MA, EMA

"""
balance = Binance.client.futures_account_balance(asset='USDT')['balance']
leverage = Binance.client.futures_change_leverage(symbol='BATUSDT', leverage=50)

#open_order = Binance.client.futures_recent_trades(symbol='BATUSDT')
#open_order_id = Binance.client.futures_recent_trades(symbol='BATUSDT')[0]['isBuyerMaker']

quant = Binance.client.futures_get_all_orders(symbol='BATUSDT')[-1]['orderId']

"""

