
import multiprocessing
import time

start = time.perf_counter()


def do_something():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done Sleeping')


p1 = multiprocessing.Process(target=do_something)
p2 = multiprocessing.Process(target=do_something)

p1.start()
p2.start()

finish = time.perf_counter()

<<<<<<< HEAD
print(f'Finisged in {round(finish-start, 4)} second(s)')
=======

print(f'Finisged in {round(finish-start, 2)} second(s)')
>>>>>>> b131b730a07452bebe8bbb5f70312605ce1e160b
