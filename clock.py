import bot1
import bot2
import bot3
from apscheduler.schedulers.blocking import BlockingScheduler
import subprocess
import time

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-sun', hour = '0-23', minute = '0-59')
def timed_job():
    p = subprocess.Popen(['python bot1.py'])
    p.terminate()
    q = subprocess.Popen(['python bot2.py'])
    q.terminate()
    r = subprocess.Popen(['python bot3.py'])
    r.terminate()

sched.start()