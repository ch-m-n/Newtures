import bot1
import bot2
import bot3
import bot4
import threading
import time
import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
    
def con():
    print(datetime.datetime.now())
    t1 = threading.Thread(target=bot1.run_trx())
    t2 = threading.Thread(target=bot2.run_bat())
    t3 = threading.Thread(target=bot3.run_xlm())
    t4 = threading.Thread(target=bot4.run_iota())
    t1.start()
    t2.start()
    t3.start()
    t4.start()

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-sun', hour = '0-23', minute = '0-59/15', max_instances=5)
def timed_job():
    con()
        

sched.start()
