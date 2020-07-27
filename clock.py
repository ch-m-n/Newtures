import bot
import threading
import time
import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
import list

    
def con():
    print(datetime.datetime.now())
    t1 = threading.Thread(target=bot.run_trx(pair=list.trx['symbol'], 
                                                q=list.trx['quote'], 
                                                b=list.trx['base'], 
                                                step=list.trx['step'],
                                                levr=list.trx['leverage'],
                                                t=list.trx['interval'],
                                                r=list.trx['roundQuant']))
    t2 = threading.Thread(target=bot.run_bat(pair=list.bat['symbol'], 
                                                q=list.bat['quote'], 
                                                b=list.bat['base'], 
                                                step=list.bat['step'],
                                                levr=list.bat['leverage'],
                                                t=list.bat['interval'],
                                                r=list.bat['roundQuant']))
    t3 = threading.Thread(target=bot.run_xlm(pair=list.xlm['symbol'], 
                                                q=list.xlm['quote'], 
                                                b=list.xlm['base'], 
                                                step=list.xlm['step'],
                                                levr=list.xlm['leverage'],
                                                t=list.xlm['interval'],
                                                r=list.xlm['roundQuant']))
    t4 = threading.Thread(target=bot.run_iota(pair=list.iota['symbol'], 
                                                q=list.iota['quote'], 
                                                b=list.iota['base'], 
                                                step=list.iota['step'],
                                                levr=list.iota['leverage'],
                                                t=list.iota['interval'],
                                                r=list.iota['roundQuant']))
    t1.start()
    t2.start()
    t3.start()
    t4.start()

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-sun', hour = '0-23', minute = '0-59/15', max_instances=5)
def timed_job():
    con()
        

sched.start()
