from apscheduler.schedulers.blocking import BlockingScheduler
import bot
import datetime

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-sun', hour = ‘0–24’, minute = ‘0–59/15’)
def timed_job():
    bot.main()

sched.start()
