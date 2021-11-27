import sys

from PySide6.QtCore import QObject, QRunnable, QThreadPool, Signal

from src.utils.logger import Logger

log = Logger(__name__)


class Pool:
    def __init__(self):
        self.pool = QThreadPool().globalInstance()

    def get_thread_count(self):
        return self.pool.maxThreadCount()

    def run(self, worker):
        self.pool.start(worker)

    def exit(self):
        log.debug("waiting for threads..")
        self.pool.waitForDone()


class WorkerSignals(QObject):
    resolve = Signal(object)
    reject = Signal(tuple)


class Worker(QRunnable):
    def __init__(self, fn, *args, **kwargs):
        super().__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

    def run(self):
        try:
            res = self.fn(*self.args, **self.kwargs)
        except Exception:
            exc_type, exception, exc_trace = sys.exc_info()
            return self.signals.reject.emit(exception)

        self.signals.resolve.emit(res)


pool = Pool()
