import pybind_multithreading
import time

_num = 600000000

def increment():
    x = 0
    for _ in range(_num):
        x += 1
    return x

class B(pybind_multithreading.A):
    def __init__(self, num):
        pybind_multithreading.A.__init__(self, num)
        self.num = num
        self.result = 0

    # python only function
    def addMore(self, x):
        self.result += x


if __name__ == "__main__":
    start_time = time.time()
    res = increment()
    print("Single thread runtime in python:" , time.time() - start_time)

    start_time = time.time()
    thread_res = pybind_multithreading.increment_cpp(_num)
    print("Single thread runtime in C++ using pybind11:" , time.time() - start_time)

    start_time = time.time()
    b = B(_num)
    goalNumber = b.multi_task()
    b.result = goalNumber
    b.addMore(1)
    print("1 more than _num:", b.result)
    print("Multithread runtime in C++ using pybind11 to derive class B from C++ class A:" , time.time() - start_time)

    print("All runs returned same result:", (res == thread_res == goalNumber))


    
