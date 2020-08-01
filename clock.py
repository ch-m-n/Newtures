import strategy
import threading
import time
import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
import list

trx = list.trx
bat = list.bat
xlm = list.xlm
iota = list.iota

def con():
    print(datetime.datetime.now())
    t1 = threading.Thread(target=strategy.run(**trx))
    t2 = threading.Thread(target=strategy.run(**bat))
    t3 = threading.Thread(target=strategy.run(**xlm))
    t4 = threading.Thread(target=strategy.run(**iota))
    t1.start()
    t2.start()
    t3.start()
    t4.start()

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-sun', hour = '0-23', minute = '0-59/15', max_instances=15, misfire_grace_time=3600)
def timed_job():
    con()
        

sched.start()
