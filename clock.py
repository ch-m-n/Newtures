from apscheduler.schedulers.blocking import BlockingScheduler
import subprocess
import time

sched = BlockingScheduler()


@sched.scheduled_job('cron', day_of_week='mon-sun', hour = '0-23', minute = '0-59/15')
def timed_job():
    p = subprocess.call(['python TRXUSDT.py'],shell=True)
    q = subprocess.call(['python BNBUSDT.py'],shell=True)
    r = subprocess.call(['python BATUSDT.py'],shell=True)

sched.start()
