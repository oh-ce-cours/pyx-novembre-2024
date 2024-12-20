import time
from multiprocessing import Pool


def compute(x):
    time.sleep(1)
    return x * x


if __name__ == "__main__":
    with Pool(5) as p:
        print(p.map(compute, range(10)))
