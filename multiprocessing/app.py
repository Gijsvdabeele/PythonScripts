import os
import time
import sys
from multiprocessing import Process

size = 1000000000

add = 0
on = True
start = time.time()


def single():
    global add
    for i in range(size):
        add += 1
    end = time.time()
    print(add)
    print("Done in " + str(round(end - start)) + " seconds.")


def loop_a():
    global add
    for i in range(int(size/4)):
        add += 1
    end = time.time()
    print(add)
    print("#1 Done in " + str(round(end - start)) + " seconds.")


def loop_b():
    global add
    for i in range(int(size/4)):
        add += 1
    end = time.time()
    print(add)
    print("#2 Done in " + str(round(end - start)) + " seconds.")


def loop_c():
    global add
    for i in range(int(size/4)):
        add += 1
    end = time.time()
    print(add)
    print("#3 Done in " + str(round(end - start)) + " seconds.")


def loop_d():
    global add
    for i in range(int(size/4)):
        add += 1
    end = time.time()
    print(add)
    print("#4 Done in " + str(round(end - start)) + " seconds.")


def threads():
    """ Returns the number of available threads on a posix/win based system """
    if sys.platform == 'win32':
        return int(os.environ['NUMBER_OF_PROCESSORS'])
    else:
        return int(os.popen('grep -c cores /proc/cpuinfo').read())


if __name__ == '__main__':
    print(threads())
    Process(target=loop_a).start()
    Process(target=loop_b).start()
    Process(target=loop_c).start()
    Process(target=loop_d).start()
