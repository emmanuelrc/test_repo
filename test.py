
import time

start = time.perf_counter()


def do_something():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done Sleeping')

do_something()

finish = time.perf_counter()


print(f'Finisged in {round(finish-start, 4)} second(s)')

