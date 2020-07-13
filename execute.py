import bot
import bip
import higherFrame
import batusdtFrame
import datetime
import time

if __name__ == '__main__':
    while True:
        if datetime.datetime.now().minute % 15 == 0:
            higherFrame.main()
            batusdtFrame.main()
            bot.main()
            bip.main()
        time.sleep(60)