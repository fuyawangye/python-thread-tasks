#! /usr/bin/env python
#! coding:utf-8
import threading
import time
from threading import Thread


lock = threading.Lock()
jobs = [1,2,3,4,5,6,7]  # 任务

# 全局配置文件
config = {
    "THREAD_NUM": 3,  # 线程数
    "LOG_FILE": "exec.log"  # 日志路径
}


def run_job(job):
    time.sleep(3)
    print("run_job:" + str(job))

# def run_jobs(lock):
#     while True:
#         lock.acquire()
#         if len(jobs) == 0:
#             lock.release()
#             break
#         job = jobs.pop()
#         lock.release()
#         try:
#             run_job(job)
#         except Exception as e:
#             print('执行任务: {0} 出错'.format(job))

# def get_threads(num, func, lock):
#     for i in range(num):
#         yield Thread(target=func, args=(lock, ))

# def main():
#     for i in get_threads(config['THREAD_NUM'], run_jobs, lock):
#         i.start()
from jobs_threads_run import JobsThreadsRun

def main():
    run = JobsThreadsRun([1,2,3,4,5,56,6], run_job, 5)
    run.start()

if __name__ == "__main__":
    main()