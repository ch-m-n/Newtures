from apscheduler.schedulers.blocking import BlockingScheduler
import subprocess
import time

sched = BlockingScheduler()


@sched.scheduled_job('cron', day_of_week='mon-sun', hour = '0-23', minute = '0-59/15')

def timed_job():
    subprocess.Popen(['python TRXUSDT.py'],shell=True)
    time.sleep(1)

    subprocess.Popen(['python BNBUSDT.py'],shell=True)
    time.sleep(1)
    
    subprocess.Popen(['python BATUSDT.py'],shell=True)
    time.time(1)

sched.start()
