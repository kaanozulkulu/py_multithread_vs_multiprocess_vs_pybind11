# Python Multithread vs Multiprocess vs Multithreading using pybind11

**High Level Explanations of Multithreading and Multiprocessing in Python for CPU bound tasks:**

**Multithreading** <br>
The python thread module does provide concurrency, however the Python GIL (Global Interpreter Lock) prevents the threads from running in parallel as each thread has to wait for the GIL to be released and then acquire it in order to run. The GIL is basically passed between the threads after a certain number of operations or after a set time (whichever comes first). This is what provides the concurrency but it does not provide any perfomance benefits for CPU bound tasks. Running 'simple_multithreading.py' shows the runtime for completing the same task with a single thread and two threads. On average the results will be similar. <br>
Example output for _num = 100,000,000 is below: <br>
  > Single thread runtime: 4.856109142303467 <br>
    Multi thread runtime: 4.702631235122681 <br>
    Multithread and single thread returned same result: True <br>

**Multiprocessing** <br>
The python multiprocessing module provides concurrency along with performance improvements for CPU bound tasks as processes are run in parallel. The issue with the GIL in threading does not apply here as each process has its own GIL and are run separately. This also means that the memory spaces are separate and it is best to write code where processes do not have a shared state. However if needed one can have a shared state or do message passing between processes (this will affect performance negatively but can still outperform serial execution depending on the task). Running 'simple_multiprocessing.py' shows the runtime for completing the same task with a single process, two processes and four processes. With more processes the task will be completed quicker, however the rate of runtime improvement will not always increase as the number of processes increases. <br>
Example output for _num = 100,000,000 is below: <br>
 >  Single process runtime: 4.85234808921814 <br>
    Multiprocess runtime with 2 processes: 2.902682065963745 <br>
    Multiprocess runtime with 4 processes: 1.6929938793182373 <br>
    Multiprocess and single process returned same result: True <br>

**Multithreading using pybind11** <br>
[pybind11](https://github.com/pybind/pybind11) enables exposing C++ types in Python. By binding C++ and python using pybind11 we can have a python project where complex tasks are executed using multithreading in C++. This will dramatically improve our runtime. Running "multithread_pybind.py" (located inside [simple_pybind_multithreading](/simple_pybind_multithreading)), shows the runtime for completing the same task with a single thread in python, single thread in C++ and four threads in C++. All the final results are accessible in our python code. Please run "cmake" to create the required CMakeFiles and "make" to create the python binding binary before running "multithread_pybind.py". <br>
Example output for _num = 100,000,000 is below: <br>
  > Single thread runtime in python: 4.745443820953369 <br>
    Single thread runtime in C++ using pybind11: 0.17310094833374023 <br>
    Multithread (four threads) runtime in C++ using pybind11: 0.04651689529418945 <br>
    All runs returned same result: True
