import signal
import time
from contextlib import contextmanager


class TimeoutException(Exception):
    pass


@contextmanager
def time_limit(seconds):
    def signal_handler(signum, frame):
        raise TimeoutException("Timed out!")

    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(seconds)
    try:
        yield
    finally:
        signal.alarm(0)


def long_function_call():
    i = 0
    for i in range(10):
        print(i)
        time.sleep(1)
        i += 1


if __name__ == "__main__":
    try:
        with time_limit(1):
            long_function_call()
    except TimeoutException as e:
        print("Timed out!")
    else:
        print("Exercise solved!")
