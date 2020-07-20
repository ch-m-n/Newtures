from apscheduler.schedulers.blocking import BlockingScheduler
import subprocess
import time

sched = BlockingScheduler()


@sched.scheduled_job('cron', day_of_week='mon-sun', hour = '0-23', minute = '0-59/15')
def timed_job():
    p = subprocess.Popen(['python TRXUSDT.py'],shell=True)
    q = subprocess.Popen(['python BNBUSDT.py'],shell=True)
    r = subprocess.Popen(['python BATUSDT.py'],shell=True)

sched.start()
