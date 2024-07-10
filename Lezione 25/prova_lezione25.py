import multiprocessing
import time

def sleep():
    print(f"sono nella fun")

    time.sleep(1)

    print(f"sto uscendo dalla fun")

if __name__ == "__main__":

    tic: float = time.time()

    t1 = multiprocessing.Process(target = sleep)
    t2 = multiprocessing.Process(target = sleep)

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    toc: float = time.time()
    time_elapsed = toc - tic

    print(f"{time_elapsed = }")
