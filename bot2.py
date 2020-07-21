import pandas as pd
import Binance
import math
from talib import TRIX, EMA, ADX, RSI
import tulipy as ti
import numpy as np 


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
        self.openPosition = float(Binance.client.futures_position_information()[-5]['positionAmt'])
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
        BuySellQuant = floatPrecision(canBuySell, 0.1)
        return BuySellQuant

    def strategy(self):

        df = self.df
        #MARKET CONDITION
        blue = EMA(df['close'], timeperiod=50)
        orange = EMA(df['close'], timeperiod=200)
        bl = float(blue[499])
        ol = float(orange[499])
        
        #ADX
        adx = ADX(df['high'], df['low'], df['close'], timeperiod=14)
        adx = float(adx[499])

        #TRIX EMA
        trix = TRIX(df['close'], timeperiod=10)
        tx = float(trix[499])*100

        red = EMA(df['close'], timeperiod=7)
        trema = TRIX(red, timeperiod=10)
        tema = float(trema[499])*100

        #STOCHRSI
        rsi = RSI(df['close'], timeperiod=14)
        rsinp = rsi.values
        rsinp = rsinp[np.logical_not(np.isnan(rsinp))]
        fastd, fastk = ti.stoch(rsinp, rsinp, rsinp, 14, 5, 3)
        
        k = float(fastd[-1])
        d = float(fastk[-1])
        
        current = float(floatPrecision(df['close'][499], self.step_size))

        longSL = float(floatPrecision((current - current*0.005), self.step_size))
        longTP = float(floatPrecision((current + current*0.01), self.step_size))
        shortSL = float(floatPrecision((current + current*0.005), self.step_size))
        shortTP = float(floatPrecision((current - current*0.01), self.step_size))

        def clearOrders():
            order = Binance.client.futures_cancel_all_open_orders(
                symbol = self.symbol)
            return

        def closeSellOrder():
            orderBuy = Binance.client.futures_create_order(
                symbol = self.symbol,
                side = 'BUY',
                type = 'MARKET',
                quantity = self.baseBalance,
                reduceOnly='true')
    

        def closeBuyOrder():
            orderSell = Binance.client.futures_create_order(
                symbol = self.symbol,
                side = 'SELL',
                type = 'MARKET',
                quantity = self.baseBalance,
                reduceOnly='true')
            

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
            while adx > 25 and tx > tema and k > d:
                if self.openPosition == 0:
                    placeBuyOrder()
                    print('BUY ORDER PLACED on BAT')
                    break
                if self.openPosition > 0:
                    print('No action on BAT')
                    break

            while k < d:
                if self.openPosition > 0:
                    try:
                        closeBuyOrder()
                        print('CLOSED BUY ORDER on BAT')
                    except:
                        pass
                if self.openPosition == 0:
                    print('No action on BAT')
                    break
                
        if bl < ol:
            while adx > 25 and tx < tema and k < d:
                if self.openPosition == 0:
                    placeSellOrder()
                    print('SELL ORDER PLACED on BAT')
                    break
                if self.openPosition < 0:
                    print('No action on BAT')
                    break

            while k > d:
                if self.openPosition < 0:
                    try:
                        closeSellOrder()
                        print('CLOSED SELL ORDER on BAT')
                    except:
                        pass
                if self.openPosition == 0:
                    print('No action on BAT')
                    break
        

def main():
    symbol = 'BATUSDT'
    quote = 'USDT'
    base = 'BAT'
    step_size = 0.0001
    leverage = 50
    interval = '15m'
    step1 = start(symbol, quote, base, step_size, leverage, interval)

