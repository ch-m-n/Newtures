import pandas as pd
import time
import datetime
import Binance
import math
from talib import EMA, MA
import quou


def floatPrecision(f, n):
    n = int(math.log10(1 / float(n)))
    f = math.floor(float(f) * 10 ** n) / 10 ** n
    f = "{:0.0{}f}".format(float(f), n)
    return str(int(f)) if int(n) == 0 else f

class start:
    def __init__(self, symbol, interval):
        self.symbol = symbol
        self.interval = interval
        self.df = self.getData()
        self.baseBalance = Binance.client.futures_get_all_orders(symbol='BATUSDT')[-1]['origQty']
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

    def strategy(self):
        df =self.df
        blue = MA(df['close'], timeperiod=50)
        orange = EMA(df['close'], timeperiod=200)
        bl = float(blue[499])
        ol = float(orange[499])
        
        def closeSellOrder():
            orderBuy = Binance.client.futures_create_order(
                symbol = self.symbol,
                side = 'BUY',
                type = 'MARKET',
                quantity = self.baseBalance,
                reduceOnly='true'
                )

        def closeBuyOrder():
            orderSell = Binance.client.futures_create_order(
                symbol = self.symbol,
                side = 'SELL',
                type = 'MARKET',
                quantity = self.baseBalance,
                reduceOnly='true'
                )

        
        while ol < bl:
            quou.changeSideBull()
            if quou.marketSide == 'BULL' and quou.bullsidetimes == 0:
                """"""
                try:
                    closeSellOrder()
                except:
                    pass
                quou.changeBullTimes1()
                quou.changeBearTimes0()
                print('BULLISH')
                break
            if quou.marketSide == 'BULL' and quou.bullsidetimes == 1:
                break 
            
        while ol > bl:
            quou.changeSideBear()
            if quou.marketSide == 'BEAR' and quou.bearsidetimes == 0:
                """"""
                try:
                    closeBuyOrder()
                except:
                    pass
                quou.changeBearTimes1()
                quou.changeBullTimes0()
                print('BEARISH')
                break
            if quou.marketSide == 'BEAR' and quou.bearsidetimes == 1:
                break

def main():
    symbol = 'TRXUSDT'
    interval = '15m'
    step1 = start(symbol, interval)
