import bot1
import bot2
import bot3
import bot4
import threading
import time
import datetime
    
def con():
    print(datetime.datetime.now())
    t1 = threading.Thread(target=bot1.run_trx())
    t2 = threading.Thread(target=bot2.run_bat())
    t3 = threading.Thread(target=bot3.run_xlm())
    t4 = threading.Thread(target=bot4.run_vet())
    t1.start()
    t2.start()
    t3.start()
    t4.start()

if __name__ == '__main__':
    while True:
        if datetime.datetime.now().minute % 15 == 0:
            con()
        time.sleep(60)

