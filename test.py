#! /usr/bin/env python
#! coding:utf-8
import threading
import time
from threading import Thread


# 全局配置文件
config = {
    "THREAD_NUM": 3,  # 线程数
    "LOG_FILE": "exec.log"  # 日志路径
}

def run_job(job):
    time.sleep(3)
    print("run_job:" + str(job))

from jobs_threads_run import JobsThreadsRun

def main():
    run = JobsThreadsRun([1,2,3,4,5,56,6], run_job, 2)
    run.start()

if __name__ == "__main__":
    main()
