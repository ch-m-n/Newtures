from apscheduler.schedulers.blocking import BlockingScheduler
import subprocess
import time

sched = BlockingScheduler()


@sched.scheduled_job('cron', day_of_week='mon-sun', hour = '0-23', minute = '0-59/15')
def timed_job():
    proc = subprocess.Popen(['python TRXUSDT.py'],shell=True)
    proc.terminate()
    proc1 = subprocess.Popen(['python BNBUSDT.py'],shell=True)
    proc1.terminate()
    proc2 = subprocess.Popen(['python BATUSDT.py'],shell=True)
    proc2.terminate()

sched.start()
