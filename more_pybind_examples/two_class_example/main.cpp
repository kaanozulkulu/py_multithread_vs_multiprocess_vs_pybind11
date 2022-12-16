#include <pybind11/pybind11.h>
#include <iostream>
#include <thread>
#include <string>
#include <mutex>  

namespace py = pybind11;
using namespace std;
using namespace std::chrono;

std::mutex mtx;


int increment_cpp(int num) {
    int x = 0;
    for(int i=0; i < num; i++){
        x++;
    }
    return x;
}

int global_x = 0;

void increment_quarter(int num){
    int local_x = 0;
 
    for(int i=0; i < static_cast<int>(num/6); i++){
        local_x++;
    }
    mtx.lock();
    global_x += local_x;
    mtx.unlock();
}

class A {

    public:

        int result = 0;
       
        int num = 0;


        A(int n){ num = n; };
        
        int multi_task(){
            thread th1(increment_quarter, num);
            thread th2(increment_quarter, num);
            
            thread th3(increment_quarter, num);
            thread th4(increment_quarter, num);

            thread th5(increment_quarter, num);
            thread th6(increment_quarter, num);
           

            th1.join();
            th2.join();
            
            th3.join();
            th4.join();
            th5.join();
            th6.join();
           
            result += global_x;
            return result;
        }
};


PYBIND11_MODULE(pybind_multithreading, m) {
    m.doc() = "pybind11 multithreading plugin"; // optional module docstring

    py::class_<A>(m, "A")
        .def(py::init<int>())
        .def("multi_task", &A::multi_task);

    m.def("increment_cpp", &increment_cpp, "A function that increments a number using a single thread");
}