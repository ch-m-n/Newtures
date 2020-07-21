from apscheduler.schedulers.blocking import BlockingScheduler
import subprocess
import time
import bot1
import bot2
import bot3

sched = BlockingScheduler()


@sched.scheduled_job('cron', day_of_week='mon-sun', hour = '0-23', minute = '0-59/15')
 
def timed_job1():
    p = bot1.main()

def timed_job2():
    q = bot2.main()

def timed_job3():
    r = bot3.main()
    
sched.start()
