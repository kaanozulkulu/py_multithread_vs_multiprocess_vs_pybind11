import pybind_multithreading
import time

_num = 100000000
       
def increment():
    x = 0
    for _ in range(_num):
        x += 1
    return x

if __name__ == "__main__":
    start_time = time.time()
    res = increment()
    print("Single thread runtime in python:" , time.time() - start_time)

    start_time = time.time()
    thread_res = pybind_multithreading.increment_cpp()
    print("Single thread runtime in C++ using pybind11:" , time.time() - start_time)
    
    start_time = time.time()
    result = pybind_multithreading.multi_task()
    print("Multithread runtime in C++ using pybind11 and four threads:" , time.time() - start_time)

    print("All runs returned same result:", (res == thread_res == result))

