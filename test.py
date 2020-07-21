from apscheduler.schedulers.blocking import BlockingScheduler
import threading
import time

def trx():
    print('Not a chance')
def bat():
    print('Give up')
def bnb():
    print('Recon')

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-sun', hour = '0-23', minute = '0-59s')
def job():
    
    t1 = threading.Thread(target=trx)
    t1.start()
    t1.join()
    t2 = threading.Thread(target=bat)
    t2.start()
    t2.join()
    t3 = threading.Thread(target=bnb)
    t3.start()
    t3.join()

sched.start()