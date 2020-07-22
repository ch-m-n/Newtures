import bot1
import bot2
import bot3
from threading import Thread
import time
import datetime
    
if __name__ == '__main__':
    while True:
        if datetime.datetime.now().minute % 15 == 0 and datetime.datetime.now().second == 0:
            bot1.main()
            bot2.main()
            bot3.main()

