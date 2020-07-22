import bot1
import bot2
import bot3
import bot4
from apscheduler.schedulers.blocking import BlockingScheduler
import subprocess
import time

def con():
    bot1.run_trx()
    bot2.run_bat()
    bot3.run_xlm()
    bot4.run_vet()

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-sun', hour = '0-23', minute = '0-59/15')
def timed_job():
    con()

sched.start()
