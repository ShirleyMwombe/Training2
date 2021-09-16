import threading
import time


def breakfast():
    time.sleep(2)
    print('You finished breakfast')


def brush():
    time.sleep(3)
    print('You finished brushing')


def work():
    time.sleep(4)
    print('You finished working')


x = threading.Thread(target=breakfast)
x.start()

y = threading.Thread(target=brush)
y.start()

z = threading.Thread(target=work)
z.start()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())
