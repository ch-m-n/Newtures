import bot1
import bot2
import bot3
from apscheduler.schedulers.blocking import BlockingScheduler
import subprocess
import time

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-sun', hour = '0-23', minute = '0-59/15')
def timed_job():
    subprocess.Popen(['python bot1.py'],shell=True).wait()
    subprocess.Popen(['python bot2.py'],shell=True).wait()
    subprocess.Popen(['python bot3.py'],shell=True).wait()

sched.start()