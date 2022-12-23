import time
from contextlib import contextmanager

class cm_timer_1:
    def __init__(self):
        self.start_t = None

    def __enter__(self):
        self.start_t = time.time()

    def __exit__(self,x,y,z):
        print(f'time: {time.time() - self.start_t}')


@contextmanager
def cm_timer_2():
    pass