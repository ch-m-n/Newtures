import bot
import threading
import time
import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
import list

trx = list.trx
xlm = list.xlm
doge = list.doge

def con():
    print(datetime.datetime.now())
    t1 = threading.Thread(target=bot.run(**trx))
    t2 = threading.Thread(target=bot.run(**xlm))
    t3 = threading.Thread(target=bot.run(**doge))
    t1.start()
    t2.start()
    t3.start()


sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-sun', hour = '0-23', minute = '0-59/15', max_instances=15, misfire_grace_time=3600)
def timed_job():
    con()
        
sched.start()
