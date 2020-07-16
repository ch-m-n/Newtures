import pandas as pd
import time
import datetime
import Binance
import math
from talib import TRIX, EMA, SAR


def floatPrecision(f, n):
    n = int(math.log10(1 / float(n)))
    f = math.floor(float(f) * 10 ** n) / 10 ** n
    f = "{:0.0{}f}".format(float(f), n)
    return str(int(f)) if int(n) == 0 else f

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
        canBuySell = (float(self.quoteBalance)/float(self.df['close'][499]))*0.05*self.leverage
        BuySellQuant = floatPrecision(canBuySell, 1)
        return BuySellQuant

    def strategy(self):

        df = self.df

        blue = EMA(df['close'], timeperiod=50)
        orange = EMA(df['close'], timeperiod=200)
        bl = float(blue[499])
        ol = float(orange[499])

        trix = TRIX(df['close'], timeperiod=10)
        tx = float(trix[499])*100

        blue = EMA(df['close'], timeperiod=7)
        trema = TRIX(blue, timeperiod=10)
        tema = float(trema[499])*100

        current = float(floatPrecision(df['close'][499], self.step_size))

        longSL = float(floatPrecision((current - current*0.005), self.step_size))
        longTP = float(floatPrecision((current + current*0.01), self.step_size))
        shortSL = float(floatPrecision((current + current*0.005), self.step_size))
        shortTP = float(floatPrecision((current - current*0.01), self.step_size))

        def clearOrders():
            order = Binance.client.futures_cancel_all_open_orders(
                symbol = self.symbol)

        def closeSellOrder():
            orderBuy = Binance.client.futures_create_order(
                symbol = self.symbol,
                side = 'BUY',
                type = 'MARKET',
                quantity = self.baseBalance,
                reduceOnly='true')
            clearOrders()
            print('SELL ORDER CLOSED AT', df['close'][499])

        def closeBuyOrder():
            orderSell = Binance.client.futures_create_order(
                symbol = self.symbol,
                side = 'SELL',
                type = 'MARKET',
                quantity = self.baseBalance,
                reduceOnly='true')
            clearOrders()
            print('SELL ORDER CLOSED AT', df['close'][499])

        def placeSellOrder():
            orderSell = Binance.client.futures_create_order(
                symbol = self.symbol,
                side = 'SELL',
                type = 'MARKET',
                quantity = self.Quant)

        def placeBuyOrder():
            orderBuy = Binance.client.futures_create_order(
                symbol = self.symbol,
                side = 'BUY',
                type = 'MARKET',
                quantity = self.Quant)

        def longStop():
            order = Binance.client.futures_create_order(
                symbol = self.symbol,
                side = 'SELL',
                type = 'STOP_MARKET',
                stopPrice = longSL,
                closePosition='true')

        def shortStop():
            order = Binance.client.futures_create_order(
                symbol = self.symbol,
                side = 'BUY',
                type = 'STOP_MARKET',
                stopPrice = shortSL,
                closePosition='true')

        def longProfit():
            order = Binance.client.futures_create_order(
                symbol = self.symbol,
                side = 'SELL',
                type = 'TAKE_PROFIT_MARKET',
                stopPrice = longTP,
                closePosition='true')

        def shortProfit():
            order = Binance.client.futures_create_order(
                symbol = self.symbol,
                side = 'BUY',
                type = 'TAKE_PROFIT_MARKET',
                stopPrice = shortTP,
                closePosition='true')

        if bl > ol:
            while tx > tema:
                if self.openPosition == 0:
                    clearOrders()
                    longStop()
                    longProfit()
                    placeBuyOrder()
                    print('BUY ORDER PLACED')
                    break
                if self.openPosition > 0:
                    print('NO')
                    break

            while tx < tema:
                if self.openPosition > 0:
                    try:
                        closeBuyOrder()
                    except:
                        pass
                if self.openPosition == 0:
                    print('NO')
                    break
                
        if bl < ol:
            while tx < tema:
                if self.openPosition == 0:
                    clearOrders()
                    shortStop()
                    shortProfit()
                    placeSellOrder()
                    print('SELL ORDER PLACED')
                    break
                if self.openPosition < 0:
                    print('NO')
                    break

            while tx > tema:
                if self.openPosition < 0:
                    try:
                        closeSellOrder()
                    except:
                        pass
                if self.openPosition == 0:
                    print('NO')
                    break

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
            main()
