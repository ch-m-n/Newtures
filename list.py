trx={
    "pair": "TRXUSDT",  #trading symbol
    "q": "USDT",        #quote symbol
    "b": "TRX",         #base symbol
    "step": 0.00001,    #step size is the number of numbers after decimal point
    "levr": 75,         #leverage allowed by Binance 
    "t": "15m",         #timeframe
    "r": 1,             #round up but/sell quantity to fit in the ammount number Binance allowes 
    "p": 6              #position is the number in position list of Binance Python API wrapper, 
                            #note that you should find the exact position of the symbol or else it will effect badly to your trades and probaly damn your account  
}

bat={
    "pair": "BATUSDT",
    "q": "USDT",
    "b": "BAT",
    "step": 0.0001,
    "levr": 50,
    "t": "15m",
    "r": 0.1,
    "p": 19
}

xlm={
    "pair": "XLMUSDT",
    "q": "USDT",
    "b": "XLM",
    "step": 0.00001,
    "levr": 50,
    "t": "15m",
    "r": 1,
    "p": 9
}

iota={
    "pair": "IOTAUSDT",
    "q": "USDT",
    "b": "IOTA",
    "step": 0.0001,
    "levr": 50,
    "t": "15m",
    "r": 0.1,
    "p": 18
}

