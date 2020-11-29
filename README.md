# async_loop

Sample project using asyncio

### Project

Create virtualenv for the project, activate it and install requirements.txt:

```
$ virtualenv -p /usr/bin/python3 venv
$ . ./venv/bin/activate
(venv)$ pip3 install -r requirements.txt
```

execute the project
```
(venv)$ python3 src/main.py
[2020-11-29 16:22:44,075]INFO main() main.py:107 version: 0.0.1 - Ctrl+C to close me.
[2020-11-29 16:22:44,075]INFO __create_fast_task() main.py:60 [FAST TASK] - random number: 2
[2020-11-29 16:22:44,075]INFO __create_slow_task() main.py:66 [SLOW TASK] - random number: 173
[2020-11-29 16:22:45,077]INFO __create_fast_task() main.py:60 [FAST TASK] - random number: 4
[2020-11-29 16:22:46,079]INFO __create_fast_task() main.py:60 [FAST TASK] - random number: 7
[2020-11-29 16:22:47,080]INFO __create_fast_task() main.py:60 [FAST TASK] - random number: 5
[2020-11-29 16:22:48,082]INFO __create_fast_task() main.py:60 [FAST TASK] - random number: 3
[2020-11-29 16:22:49,079]INFO __create_slow_task() main.py:66 [SLOW TASK] - random number: 135
[2020-11-29 16:22:49,085]INFO __create_fast_task() main.py:60 [FAST TASK] - random number: 7
[2020-11-29 16:22:50,087]INFO __create_fast_task() main.py:60 [FAST TASK] - random number: 6
[2020-11-29 16:22:51,088]INFO __create_fast_task() main.py:60 [FAST TASK] - random number: 2
[2020-11-29 16:22:52,090]INFO __create_fast_task() main.py:60 [FAST TASK] - random number: 5
[2020-11-29 16:22:53,092]INFO __create_fast_task() main.py:60 [FAST TASK] - random number: 5
[2020-11-29 16:22:54,082]INFO __create_slow_task() main.py:66 [SLOW TASK] - random number: 127
[2020-11-29 16:22:54,094]INFO __create_fast_task() main.py:60 [FAST TASK] - random number: 2
[2020-11-29 16:22:55,094]INFO __create_fast_task() main.py:60 [FAST TASK] - random number: 3
[2020-11-29 16:22:56,099]INFO __create_fast_task() main.py:60 [FAST TASK] - random number: 6
[2020-11-29 16:22:57,100]INFO __create_fast_task() main.py:60 [FAST TASK] - random number: 9
[2020-11-29 16:22:58,103]INFO __create_fast_task() main.py:60 [FAST TASK] - random number: 9
[2020-11-29 16:22:59,094]INFO __create_slow_task() main.py:66 [SLOW TASK] - random number: 121
[2020-11-29 16:22:59,106]INFO __create_fast_task() main.py:60 [FAST TASK] - random number: 5
[2020-11-29 16:23:00,110]INFO __create_fast_task() main.py:60 [FAST TASK] - random number: 7
[2020-11-29 16:23:01,112]INFO __create_fast_task() main.py:60 [FAST TASK] - random number: 1
[2020-11-29 16:23:02,114]INFO __create_fast_task() main.py:60 [FAST TASK] - random number: 7
[2020-11-29 16:23:03,115]INFO __create_fast_task() main.py:60 [FAST TASK] - random number: 3
[2020-11-29 16:23:04,099]INFO __create_slow_task() main.py:66 [SLOW TASK] - random number: 156
[2020-11-29 16:23:04,117]INFO __create_fast_task() main.py:60 [FAST TASK] - random number: 10
[2020-11-29 16:23:05,119]INFO __create_fast_task() main.py:60 [FAST TASK] - random number: 1
^C[2020-11-29 16:23:05,431]INFO __close_tasks() main.py:53 <Task cancelled name='Task-1' coro=<LoopApp.__create_fast_task() done, defined at src/main.py:57>> has been canceled now.
[2020-11-29 16:23:05,432]INFO __close_tasks() main.py:53 <Task cancelled name='Task-2' coro=<LoopApp.__create_slow_task() done, defined at src/main.py:63>> has been canceled now.

```



### References

https://docs.python.org/3.8/library/asyncio.html
https://realpython.com/async-io-python/
