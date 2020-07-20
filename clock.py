from apscheduler.schedulers.blocking import BlockingScheduler
import subprocess
import time

sched = BlockingScheduler()


@sched.scheduled_job('cron', day_of_week='mon-sun', hour = '0-23', minute = '0-59/15')
def timed_job():
    proc = subprocess.Popen(['python TRXUSDT.py'],shell=True)
    try:
        proc.wait(timeout=0.3)
    except subprocess.TimeoutExpired:
        proc.terminate()
    proc1 = subprocess.Popen(['python BNBUSDT.py'],shell=True)try:
        proc1.wait(timeout=0.3)
    except subprocess.TimeoutExpired:
        proc1.terminate()
    proc2 = subprocess.Popen(['python BATUSDT.py'],shell=True)
    try:
        proc2.wait(timeout=0.3)
    except subprocess.TimeoutExpired:
        proc2.terminate()

sched.start()
