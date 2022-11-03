import time
import threading

# global variables
x_1 = 0
x_2 = 0

_num = 100000000

def increment():
    x = 0
    for _ in range(_num):
        x += 1
    return x

def thread_1(lock):
    local_x = 0
    for _ in range(int(_num/2)):
        local_x += 1
    lock.acquire()
    global x
    x += local_x
    lock.release()

def thread_2(lock):
    local_x = 0
    for _ in range(int(_num/2)):
        local_x += 1
    lock.acquire()
    global x
    x += local_x
    lock.release()

def multi_task():
    global x
    x = 0

    lock = threading.Lock()
  
    t1 = threading.Thread(target=thread_1, args=(lock,))
    t2 = threading.Thread(target=thread_2, args=(lock,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    return x

if __name__ == "__main__":
    start_time = time.time()
    res = increment()
    print("Single thread runtime:" , time.time() - start_time)

    start_time = time.time()
    thread_res = multi_task()
    print("Multi thread runtime:" , time.time() - start_time)

    print("Multithread and single thread returned same result:", (res == thread_res))
