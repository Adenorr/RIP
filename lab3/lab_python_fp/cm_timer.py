import time

class cm_timer_1:
    def __init__(self):
        self.start = time.monotonic()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        print('time: {}'.format(time.monotonic() - self.start))

from contextlib import contextmanager

@contextmanager
def cm_timer_2():
    start = time.monotonic()
    yield
    print('time: {}'.format(time.monotonic() - start))

def main():
    with cm_timer_1():
        time.sleep(5.5)

    with cm_timer_2():
        time.sleep(5.5)

if __name__ == "__main__":
    main()
