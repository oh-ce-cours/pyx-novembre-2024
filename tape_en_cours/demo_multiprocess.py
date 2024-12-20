import time
from multiprocessing import Pool


def compute(x):
    time.sleep(10)
    return x * x


if __name__ == "__main__":
    with Pool(10) as p:
        print(p.map(compute, range(10)))
