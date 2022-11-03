from multiprocessing import Pool
import time
import numpy as np

_num = 100000000

def increment():
    x = 0
    for _ in range(_num):
        x += 1
    return x

def half_process(x):
    for _ in range(int(_num/2)):
        x += 1
    return x

def quarter_process(x):
    for _ in range(int(_num/4)):
        x += 1
    return x

def multi_task_half():
    x = 0
    y = 0

    with Pool(2) as pool:
        result = pool.map(half_process, [x, y])
    
    final_result = np.sum(result)
    return final_result

def multi_task_quarter():
    x = 0
    y = 0
    z = 0
    k = 0

    with Pool(4) as pool:
        result = pool.map(quarter_process, [x, y, z, k])
    
    final_result = np.sum(result)
    return final_result
    
if __name__ == "__main__":

    start_time = time.time()
    res = increment()
    print("Single process runtime:" , time.time() - start_time)

    start_time = time.time()
    res_half = multi_task_half()
    print("Multiprocess runtime with 2 processes:" , time.time() - start_time)

    start_time = time.time()
    res_quarter = multi_task_quarter()
    print("Multiprocess runtime with 4 processes:" , time.time() - start_time)

    print("Multiprocess and single process returned same result:", (res == res_half == res_quarter))

