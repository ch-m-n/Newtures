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
        if datetime.datetime.now().minute % 15 == 0 and datetime.datetime.now().second == 0:
            bot1.main()
            bot2.main()
            bot3.main()
            bot4.main()
        time.sleep(sleeptime)