import datetime
import time
import bot1
import bot2
import bot3

if __name__ == '__main__':
    while True:
        if datetime.datetime.now().minute % 15 == 0: 
            bot1.main()
            bot2.main()
            bot3.main()
        time.sleep(1)
