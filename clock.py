import bot1
import bot2
import bot3
import bot4
from threading import Thread
import time
import datetime
import sys
    
t = datetime.datetime.now()
sleeptime = 60 - (t.second + t.microsecond/1000000.0)

if __name__ == '__main__':
    while True:
        if datetime.datetime.now().minute % 1 == 0:
            bot1.run_trx()
            bot2.run_bat()
            bot3.run_xlm()
            bot4.run_vet()
        time.sleep(sleeptime)