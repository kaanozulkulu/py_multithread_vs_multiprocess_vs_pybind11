import pybind_multithreading
import time

_num = 600000000  #600,000,000

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
    thread_res = pybind_multithreading.increment_cpp(_num)
    print("Single thread runtime in using pybind11:" , time.time() - start_time)

    start_time = time.time()
    p = pybind_multithreading.A()
    # print(p.getNum())
    p.setNum(_num)
    # print(p.getNum())
    result = p.multi_task()

    print("Multithread runtime using pybind11 to call C++ class A's multithreaded function in python:" , time.time() - start_time)

    print("All runs returned same result:", (res == thread_res == result))

