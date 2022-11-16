#include <pybind11/pybind11.h>
#include <iostream>
#include <thread>
#include <string>
#include <mutex>  

namespace py = pybind11;
using namespace std;
using namespace std::chrono;

std::mutex mtx;

int const NUM = 100000000; 
int global_x = 0;

int increment_cpp() {
    int x = 0;
    for(int i=0; i < NUM; i++){
        x++;
    }
    return x;
}

void thread_1(){
    int local_x = 0;
    for(int i=0; i < static_cast<int>(NUM/4); i++){
        local_x++;
    }
    mtx.lock();
    global_x += local_x;
    mtx.unlock();
}

void thread_2(){
    int local_x = 0;
    for(int i=0; i < static_cast<int>(NUM/4); i++){
        local_x++;
    }
    mtx.lock();
    global_x += local_x;
    mtx.unlock();
}

void thread_3(){
    int local_x = 0;
    for(int i=0; i < static_cast<int>(NUM/4); i++){
        local_x++;
    }
    mtx.lock();
    global_x += local_x;
    mtx.unlock();
}

void thread_4(){
    int local_x = 0;
    for(int i=0; i < static_cast<int>(NUM/4); i++){
        local_x++;
    }
    mtx.lock();
    global_x += local_x;
    mtx.unlock();
}

int multi_task(){
    thread th1(thread_1);
    thread th2(thread_2);
    
    thread th3(thread_3);
    thread th4(thread_4);

    th1.join();
    th2.join();
    
    th3.join();
    th4.join();

    return global_x;
}

PYBIND11_MODULE(pybind_multithreading, m) {
    m.doc() = "pybind11 multithreading plugin"; // optional module docstring

    m.def("increment_cpp", &increment_cpp, "A function that increments a number using a single thread");
    m.def("multi_task", &multi_task, "A function that increments a number using multithreading");
}