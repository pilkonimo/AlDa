import math
import random
import numpy as np


def createData(size):
    a = []
    while len(a) < size:
        x,y = random.uniform(-1, 1), random.uniform(-1, 1)
        r = math.sqrt(x**2 + y**2)
        if r < 1.0:
            a.append(r)
    return a

def bucketMap(r, M):
    return int(r**2 * M)

def bucketMaplin(r, M):
    return int(r * M)

def createBuckets(data, M):
    indexes = [bucketMap(r, M) for r in data]
    bucket_lens = [None] * M

    for index in range(M):
        bucket_lens[index] = indexes.count(index)

    return bucket_lens

def createBucketslin(data, M):
    indexes = [bucketMaplin(r, M) for r in data]
    bucket_lens = [None] * M

    for index in range(M):
        bucket_lens[index] = indexes.count(index)

    return bucket_lens

def chi2Test(bucket_lens, N):
    M = len(bucket_lens)
    c = N / M

    chi2 = np.sum((np.array(bucket_lens) - c)**2 / c)
    tau = np.sqrt(2*chi2) - np.sqrt(2 * M - 3)

    if abs(tau) > 3:
        return False
    else:
        return True

def task2_b():
    a = createData(random.randint(10, 100))
    b = createData(random.randint(100,1000))
    c = createData(random.randint(1000,10000))

    N_a = len(a)
    print(N_a)
    N_b = len(b)
    N_c = len(c)

    M_array = [10, 100, 500]

    for M in M_array:
        #r^2 BucketMap Funktion
        print('bM r^2, data=ran(10,100),     N = {:}, M = {:}, Test bestanden: '.format(N_a, M), chi2Test(createBuckets(a, M), N_a))
        print('bM r^2, data=ran(100,1000),   N = {:}, M = {:}, Test bestanden: '.format(N_b, M), chi2Test(createBuckets(b, M), N_b))
        print('bM r^2, data=ran(1000,10000), N = {:}, M = {:}, Test bestanden: '.format(N_c, M), chi2Test(createBuckets(c, M), N_c))

    print()

    for M in M_array:
        #lineare BucketMaplin Funktion
        print('bM r  , data=ran(10,100),     N = {:}, M = {:}, Test bestanden: '.format(N_a, M), chi2Test(createBucketslin(a, M), N_a))
        print('bM r  , data=ran(100,1000),   N = {:}, M = {:}, Test bestanden: '.format(N_b, M), chi2Test(createBucketslin(b, M), N_b))
        print('bM r  , data=ran(1000,10000), N = {:}, M = {:}, Test bestanden: '.format(N_c, M), chi2Test(createBucketslin(c, M), N_c))



if __name__ == '__main__':
    task2_b()