from apscheduler.schedulers.blocking import BlockingScheduler
import bot
import datetime

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=15)
def timed_job():
    bot.main()

sched.start()
