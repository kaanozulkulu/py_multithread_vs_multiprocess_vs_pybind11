# python_multithread_vs_multiprocess

High Level Explanations of Multithreading and Multiprocessing in Python for CPU heavy tasks:

Multithreading
The python thread module does provide concurrency, however the GIL (Global Interpreter Lock) prevents the threads from running in parallel as each thread has to wait for the GIL to be released and then acquire it in order to run. The GIL is basically passed between the threads after a certain number of operations or after a set time (whichever comes first). This is what provides the concurrency but it does not provide any perfomance benefits for CPU heavy tasks. Running 'simple_multithreading.py' shows the runtime for completing the same task with a single thread and two threads. On average the results will be similar. 
Example output for _num = 100,000,00 is below:
    Single thread runtime: 4.856109142303467
    Multi thread runtime: 4.702631235122681
    Multithread and single thread returned same result: True

Multiprocessing
The python multiprocessing module provides concurrency along with performance improvements for CPU heavy tasks as processes are run in parallel. The issue with the GIL in threading does not apply here as each process has its own GIL and are run separately. This also means that the memory spaces are separate and it is best to write code where processes do not have a shared state. However if needed one can have a shared state or do message passing between processes (this will affect performance negatively but can still outperform serial execution depending on the task). Running 'simple_multiprocessing.py' shows the runtime for completing the same task with a single process, two processes and four processes. With more processes the task will be completed quicker, however the rate of runtime improvement will not always increase as number of processes increases.
Example output for _num = 100,000,00 is below:
    Single process runtime: 4.85234808921814
    Multiprocess runtime with 2 processes: 2.902682065963745
    Multiprocess runtime with 4 processes: 1.6929938793182373
    Multiprocess and single process returned same result: True

