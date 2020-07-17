from apscheduler.schedulers.blocking import BlockingScheduler
import bot

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-sun', hour = '0-23', minute = '0-59/15')


sched.start()
