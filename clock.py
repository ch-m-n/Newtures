import bot1
import bot2
import bot3
from apscheduler.schedulers.blocking import BlockingScheduler
from threading import Thread
import time

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-sun', hour = '0-23', minute = '0-59/15')
def job():
    
    t1 = Thread(target=bot1.main())
    t2 = Thread(target=bot2.main())
    t3 = Thread(target=bot3.main())
    t1.start()
    t2.start()
    t3.start()

sched.start()