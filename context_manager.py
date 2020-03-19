from utils import test_execution


COUNT = 8000


@test_execution('with context manager')
def with_context_manager():
    def runner():
        for _ in range(COUNT):
            with open('test.txt', 'r') as file:
                content = file.read()
    return runner


@test_execution('without context manager')
def without_context_manager():
    def runner():
        for _ in range(COUNT):
            file = open('test.txt', 'r')
            content = file.read()
            file.close()
    return runner


def main():
    with_context_manager()
    without_context_manager()


if __name__ == '__main__':
    main()
