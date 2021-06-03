from hangzhou_jobs import get_hangzhou_jobs
from zhejiang_jobs import get_zhejiang_jobs
from zj_college_jobs import get_college_jobs
import time
from threading import Thread


def workday2day(workdays):
    days = workdays // 7 * 2 + workdays
    localtime = time.localtime(time.time())
    if localtime.tm_wday < workdays:
        days = days + 2
    return days


print("Spider is working. Please wait!")
last_days = workday2day(3)
threads = [
    Thread(target=get_zhejiang_jobs, args=(last_days,)),
    Thread(target=get_hangzhou_jobs, args=(last_days,)),
    Thread(target=get_college_jobs, args=(last_days,))
]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print("Done!!!")
