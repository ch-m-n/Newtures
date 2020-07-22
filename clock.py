import bot1
import bot2
import bot3
from threading import Thread
import time
import datetime
    
if __name__ == '__main__':
    while True:
        if datetime.datetime.now().minute % 15 == 0 and datetime.datetime.now().second == 0:
            t1 = Thread(target=bot1.main())
            t2 = Thread(target=bot2.main())
            t3 = Thread(target=bot3.main())
            t1.start()
            t2.start()
            t3.start()
