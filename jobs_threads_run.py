#! coding:utf-8
import threading
import copy
import logging
from threading import Thread
from types import FunctionType


class JobsThreadsRun(object):
    """
    多线程取jobs，并执行函数
    """
    def __init__(self, jobs, func, num_threads=2):
        if not isinstance(jobs, list):
            raise ValueError("Jobs 参数必须是个List: {}".format(type(jobs)))
        if not isinstance(func, FunctionType):
            raise ValueError("func 必须是一个函数对象用于执行job: {}".format(type(func)))
        self.jobs = jobs
        self.unfinish_jobs = copy.deepcopy(self.jobs)
        self.error_jobs = []
        self.success_jobs = []
        self.run_func = func
        self.thread_num = num_threads
        self.__lock = threading.Lock()
        self._current_threads = []

    def start(self):
        for i in self._get_threads():
            i.start()

    def _get_threads(self):
        for i in range(self.thread_num):
            temp = Thread(target=self._run_threads)
            self._current_threads.append(temp)
        return self._current_threads

    def _run_threads(self):
        while True:
            self.__lock.acquire()
            if len(self.unfinish_jobs) == 0:
                self.__lock.release()
                break
            job = self.unfinish_jobs.pop()
            self.__lock.release()
            try:
                self.run_func(job)
                self.success_jobs.append(job)
            except Exception as e:
                self.error_jobs.append((job, e))
