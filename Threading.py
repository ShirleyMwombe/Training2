# thread =  a flow of execution. Like a separate order of instructions.
#                  However each thread takes a turn running to achieve concurrency
#                  GIL = (global interpreter lock),
#                  allows only one thread to hold the control of the Python interpreter at any one time

# cpu bound = program/task spends most of it's time waiting for internal events (CPU intensive)
#             use multiprocessing

# io bound = program/task spends most of it's time waiting for external events (user input, web scraping)
#            use multithreading == threads run concurrently, not in parallel. Run while the other is idle

import threading
import time


def breakfast():
    time.sleep(3)
    print('You finished taking breakfast')


def brush():
    time.sleep(4)
    print('You finished brushing')


def work():
    time.sleep(5)
    print('You finished work')


# breakfast()
# brush()
# work()  #executes sequentially


# execute concurrently---

x = threading.Thread(target=breakfast, args=())  # input arguments if it has parameters
x.start()  # to begin the thread

y = threading.Thread(target=brush, args=())
y.start()

z = threading.Thread(target=work, args=())
z.start()

x.join() # main thread/calling thread wait for the thread
y.join()
z.join()

print(threading.active_count())  # number of threads currently running
print(threading.enumerate())  # list of all threads currently running
print(time.perf_counter())
