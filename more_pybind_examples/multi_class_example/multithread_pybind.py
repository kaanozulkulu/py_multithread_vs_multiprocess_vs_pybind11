import pybind_multithreading
import time


_num = 600000000

def increment():
    x = 0
    for _ in range(_num):
        x += 1
    return x

class B(pybind_multithreading.C):
    # override getNum 
    def getNum(self):
        # Write number as string for pybind compatability
        return str(_num)


if __name__ == "__main__":
    start_time = time.time()
    res = increment()
    print("Single thread runtime in python:" , time.time() - start_time)

    start_time = time.time()
    thread_res = pybind_multithreading.increment_cpp(_num)
    print("Single thread runtime in C++ using pybind11:" , time.time() - start_time)
    start_time = time.time()
    b = B()
    a = pybind_multithreading.A(b)
    result = a.multi_task()
    print("Multithread runtime of class A's multi_task function that makes use of getNum() which is defined in python, pybind11 used:" , time.time() - start_time)

    print("All runs returned same result:", (res == thread_res))

    
