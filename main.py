import time
from threading import Thread
import multiprocessing


COUNT = 8000000


def countdown(n):
    while n > 0:
        n -= 1


def scheduler(tasks):
    while tasks:
        task = tasks.popleft()
        try:
            next(task)
            tasks.append(task)
        except StopIteration:
            pass


def main():
    print('with normal way')
    start = time.time()
    countdown(COUNT)
    end = time.time()
    print((end - start) * 1000)  # ms

    print('with treads')

    t1 = Thread(target=countdown, args=(COUNT/2,))
    t2 = Thread(target=countdown, args=(COUNT/2,))

    start = time.time()

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    end = time.time()

    print((end - start) * 1000)  # ms

    print('with multiprocessing')
    p = multiprocessing.Pool(2)

    start = time.time()

    task1 = p.apply_async(countdown, (COUNT / 2,))
    task2 = p.apply_async(countdown, (COUNT / 2,))

    # scheduler(tasks)

    task1.get()
    task2.get()

    end = time.time()

    print((end - start) * 1000)  # ms


if __name__ == '__main__':
    main()
