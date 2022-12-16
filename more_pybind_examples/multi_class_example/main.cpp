#include <pybind11/pybind11.h>
#include <iostream>
#include <thread>
#include <string>
#include <mutex>

namespace py = pybind11;
using namespace std;

std::mutex mtx;


int increment_cpp(int num) {
    int x = 0;
    for(int i=0; i < num; i++){
        x++;
    }
    return x;
};

//class C's virtual getNum will be defined in python
class C {
public:
    virtual ~C() { }
    virtual string getNum() = 0;
};

class PyC : public C {
public:
    /* Inherit the constructors */
    using C::C;

    /* Trampoline */
    string getNum() override {
        PYBIND11_OVERRIDE_PURE(
            string, /* Return type */
            C,      /* Parent class */
            getNum,          /* Name of function in C++ (must match Python name) */
        );
    }
};

int global_x = 0;
void increment_quarter(C *shared_obj) {
        int local_x = 0;
        
        string numString = shared_obj->getNum();

        int num = stoi(numString);
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
        C *shared_obj;
        A(C *c){ shared_obj = c; };
      
        int multi_task(){
        
            thread th1(increment_quarter, shared_obj);
            thread th2(increment_quarter, shared_obj);
            
            thread th3(increment_quarter, shared_obj);
            thread th4(increment_quarter, shared_obj);

            thread th5(increment_quarter, shared_obj);
            thread th6(increment_quarter, shared_obj);

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

    py::class_<C, PyC>(m, "C")
        .def(py::init<>())
        .def("getNum", &C::getNum);
    
    py::class_<A>(m, "A")
        .def(py::init<C*>())
        .def("multi_task", &A::multi_task, py::call_guard<py::gil_scoped_release>());
    
    
    m.def("increment_cpp", &increment_cpp, "A function that increments a number using a single thread");
}