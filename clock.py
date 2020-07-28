import bot
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
    t1 = threading.Thread(target=bot.run(**trx))
    t2 = threading.Thread(target=bot.run(**bat))
    t3 = threading.Thread(target=bot.run(**xlm))
    t4 = threading.Thread(target=bot.run(**iota))
    t1.start()
    t2.start()
    t3.start()
    t4.start()

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-sun', hour = '0-23', minute = '0-59/15', max_instances=15)
def timed_job():
    con()
        

sched.start()
