import bot
import threading
import time
import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
import list

    
def con():
    print(datetime.datetime.now())
    t1 = threading.Thread(target=bot.run(list.**trx))
    t2 = threading.Thread(target=bot.run(list.**bat))
    t3 = threading.Thread(target=bot.run(list.**xlm))
    t4 = threading.Thread(target=bot.run(list.**iota))
    t1.start()
    t2.start()
    t3.start()
    t4.start()

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-sun', hour = '0-23', minute = '0-59/15', max_instances=15)
def timed_job():
    con()
        

sched.start()
