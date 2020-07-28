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
    bot.run(**trx)
    bot.run(**bat)
    bot.run(**xlm)
    bot.run(**iota)

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-sun', hour = '0-23', minute = '0-59/15', max_instances=15)
def timed_job():
    con()
        

sched.start()
