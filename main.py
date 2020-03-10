import time
from threading import Thread
import multiprocessing


COUNT = 8000000


def countdown(n):
    while n > 0:
        n -= 1


def test_execution(msg):
    def decorator(func):
        def wrapped(*args, **kwargs):
            runner = func(*args, **kwargs)
            print(msg)
            start = time.time()
            runner()
            end = time.time()
            milliseconds = (end - start) * 1000
            print(f'{milliseconds} ms\n')
            return milliseconds
        return wrapped
    return decorator


@test_execution('with normal way')
def normal_way():
    def runner():
        countdown(COUNT)
    return runner


@test_execution('with threads')
def with_threads():
    t1 = Thread(target=countdown, args=(COUNT / 2,))
    t2 = Thread(target=countdown, args=(COUNT / 2,))

    def runner():
        t1.start()
        t2.start()
        t1.join()
        t2.join()
    return runner


@test_execution('with multiprocessing')
def with_multiprocess():
    pool = multiprocessing.Pool(2)
    half_count = COUNT / 2

    def runner():
        task1 = pool.apply_async(countdown, (half_count,))
        task2 = pool.apply_async(countdown, (half_count,))
        task1.get()
        task2.get()
    return runner


def main():
    normal_way()
    with_threads()
    with_multiprocess()


if __name__ == '__main__':
    main()
