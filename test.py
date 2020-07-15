import pandas as pd
import numpy as np
import time
import datetime
import Binance
import math
from talib import MACD, STOCH
import higherFrame
import quou

def floatPrecision(f, n):
    n = int(math.log10(1 / float(n)))
    f = math.floor(float(f) * 10 ** n) / 10 ** n
    f = "{:0.0{}f}".format(float(f), n)
    return str(int(f)) if int(n) == 0 else f

def compare(a, b):
    if a > b:
        print(a, '>', b)
    elif a < b:
        print(a, '<', b)
    elif a == b:
        print(a, '=', b)

class start:
    def __init__(self, symbol, quote, base, step_size, leverage, interval):
        self.symbol = symbol
        self.quote = quote
        self.base = base
        self.step_size = step_size
        self.leverage = leverage
        self.interval = interval
        self.df = self.getData()
        self.changeLeverage = self.changeLeverage()
        self.openPosition = float(Binance.client.futures_position_information()[6]['positionAmt'])
        self.quoteBalance = float(Binance.client.futures_account_balance(asset=self.quote)['balance'])
        self.baseBalance = float(Binance.client.futures_get_all_orders(symbol=self.symbol)[-1]['origQty'])
        self.Quant = self.checkQuant()
        self.fire = self.strategy()
        
    def getData(self):
        candles = Binance.client.futures_klines(symbol=self.symbol, interval=self.interval)

        #Sorting candlestick using Pandas
        df = pd.DataFrame(candles)
        df = df.drop(range(6, 12), axis=1)

        # put in dataframe and clean-up
        col_names = ['time', 'open', 'high', 'low', 'close', 'volume']
        df.columns = col_names
        # transform values from strings to floats
        for col in col_names:
            df[col] = df[col].astype(float)

        return df

    def changeLeverage(self):
        def change():
            change = Binance.client.futures_change_leverage(
                symbol=self.symbol, 
                leverage=self.leverage)
        return change()

    def checkQuant(self):
        df = self.df    
        canBuySell = (float(self.quoteBalance)/float(self.df['close'][499]))*0.1*self.leverage
        BuySellQuant = floatPrecision(canBuySell, 1)
        return BuySellQuant

    def strategy(self):

        df = self.df

        macd, macdsignal, macdhist = MACD(df['close'], fastperiod=7, slowperiod=21, signalperiod=3)
        macd = float(macd[499])
        sign = float(macdsignal[499])
        hist = float(macdhist[499])

        slowk, slowd = STOCH(df['high'], df['low'], df['close'], fastk_period=14, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0)

        k = float(slowk[499])
        d = float(slowd[499])

        if quou.marketSide == 'BULL':
            while macd > sign and k > d:
                if self.openPosition == 0:
                    compare(macd, sign)
                    compare(k, d)
                    print('BUY ORDER PLACED AT', df['close'][499])
                    break
            while k < d:
                if self.openPosition > 0:
                    compare(k, d)
                    print('BUY ORDER CLOSED AT', df['close'][499])

            
        if quou.marketSide == 'BEAR':
            while macd < sign and k < d:
                if self.openPosition == 0:
                    compare(macd, sign)
                    compare(k, d)
                    print('SELL ORDER PLACED AT', df['close'][499])
                    break
            while k > d:
                if self.openPosition < 0:
                    compare(k, d)
                    print('SELL ORDER CLOSED AT', df['close'][499])

def main():
    symbol = 'TRXUSDT'
    quote = 'USDT'
    base = 'TRX'
    step_size = 0.00001
    leverage = 75
    interval = '15m'
    
    step1 = start(symbol, quote, base, step_size, leverage, interval)

if __name__ == '__main__':
    while True:
        if datetime.datetime.now().minute % 15 == 0:
            higherFrame.main()
            main()
        time.sleep(60)