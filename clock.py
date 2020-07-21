from apscheduler.schedulers.blocking import BlockingScheduler
import subprocess
import time
import trxusdt
import bnbusdt
import batusdt

sched = BlockingScheduler()


@sched.scheduled_job('cron', day_of_week='mon-sun', hour = '0-23', minute = '0-59/15')
 
def timed_job():
    p = trxusdt.main()

    q = bnbusdt.main()
    q.terminate()
    
    r = batusdt.main()
    r.terminate()
    
sched.start()
