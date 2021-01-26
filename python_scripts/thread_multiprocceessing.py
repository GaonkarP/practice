import time
import threading

start = time.perf_counter()

def do_something():
    print('Sleeping for 1 second...')
    time.sleep(1)
    print('Done sleeping for 1 second...')

t1 = threading.Thread(target=do_something)
t2 = threading.Thread(target=do_something)
t1.start()
t2.start()
# do_something()
# do_something()

finish = time.perf_counter()

print(f"Finished in {round(finish - start, 2)} second(s)")