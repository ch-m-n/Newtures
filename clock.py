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
    t1.start()
    t1.join()
    t2 = threading.Thread(target=bot2.run_bat())
    t2.start()
    t2.join()
    t3 = threading.Thread(target=bot3.run_xlm())
    t3.start()
    t3.join()
    t3 = threading.Thread(target=bot4.run_vet())
    t3.start()
    t3.join()

if __name__ == '__main__':
    while True:
        if datetime.datetime.now().minute % 15 == 0:
            con()
        time.sleep(60)

