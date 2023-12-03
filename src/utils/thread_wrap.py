
import threading
from utils.pipe_queue import pipe_queue

class thread_wrap(threading.Thread):
    def __init__(self, name="noneame"):
        threading.Thread.__init__(self)
        self.name = name
        self.run_cond = True
        self.in_queue = pipe_queue("input")
        self.out_queue = pipe_queue("output")

    def is_blocking(self):
        return False

    def ask_to_stop(self):
        self.run_cond = False

    def stop(self):
        self.ask_to_stop()
        self.join()