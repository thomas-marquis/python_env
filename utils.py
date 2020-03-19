import time


def test_execution(msg):
    def decorator(func):
        def wrapped_func(*args, **kwargs):
            runner = func(*args, **kwargs)
            print(msg)
            start = time.time()
            runner()
            end = time.time()
            milliseconds = (end - start) * 1000
            print(f'{milliseconds} ms\n')
            return milliseconds
        return wrapped_func
    return decorator
