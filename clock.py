import strategy
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
<<<<<<< HEAD
    t1 = threading.Thread(target=strategy.run(**trx))
    t2 = threading.Thread(target=strategy.run(**bat))
    t3 = threading.Thread(target=strategy.run(**xlm))
    t4 = threading.Thread(target=strategy.run(**iota))
=======
    t1 = threading.Thread(target=bot.run(**trx))
    t2 = threading.Thread(target=bot.run(**xlm))
    t3 = threading.Thread(target=bot.run(**doge))
>>>>>>> 09f82f4a20f1e9c65073a5ff8d97d8ad926d556b
    t1.start()
    t2.start()
    t3.start()


sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-sun', hour = '0-23', minute = '0-59/15', max_instances=15, misfire_grace_time=3600)
def timed_job():
    con()
        
sched.start()
