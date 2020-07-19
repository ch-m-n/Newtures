import bot
from crontab import CronTab

cron = CronTab(user='username')  # Initialise a new CronTab instance
job = cron.new(command='python bot.py')  # create a new task
job.minute.on(0, 15, 30, 45)  # Define that it should be on every 0th, 15th, 30th and 45th minute

cron.write()  # 'Start' the task (i.e trigger the cron-job, but through the Python 