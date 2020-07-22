import bot1
import bot2
import bot3
import bot4
from threading import Thread
import time
import datetime
import sys
    
def con():
    print(datetime.datetime.now())
    bot1.run_trx()
    bot2.run_bat()
    bot3.run_xlm()
    bot4.run_vet()
    
if __name__ == '__main__':
    while True:
        if datetime.datetime.now().minute % 15 == 0:
            con()
        time.sleep(60)

