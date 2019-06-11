import math
import random
import numpy as np
import unittest
import copy


#### Z7 Task 2)

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

def createBucketLens(data, M):
    indexes = [bucketMap(r, M) for r in data]
    bucket_lens = [None] * M

    for index in range(M):
        bucket_lens[index] = indexes.count(index)

    return bucket_lens

def createBucketLenslin(data, M):
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

def task_2b():
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
        print('bM r^2, data=ran(10,100),     N = {:}, M = {:}, Test bestanden: '.format(N_a, M), chi2Test(createBucketLens(a, M), N_a))
        print('bM r^2, data=ran(100,1000),   N = {:}, M = {:}, Test bestanden: '.format(N_b, M), chi2Test(createBucketLens(b, M), N_b))
        print('bM r^2, data=ran(1000,10000), N = {:}, M = {:}, Test bestanden: '.format(N_c, M), chi2Test(createBucketLens(c, M), N_c))

    print()

    for M in M_array:
        #lineare BucketMaplin Funktion
        print('bM r  , data=ran(10,100),     N = {:}, M = {:}, Test bestanden: '.format(N_a, M), chi2Test(createBucketLenslin(a, M), N_a))
        print('bM r  , data=ran(100,1000),   N = {:}, M = {:}, Test bestanden: '.format(N_b, M), chi2Test(createBucketLenslin(b, M), N_b))
        print('bM r  , data=ran(1000,10000), N = {:}, M = {:}, Test bestanden: '.format(N_c, M), chi2Test(createBucketLenslin(c, M), N_c))


#### Task c)


def insertionSort(a, key=lambda x: x):
    for i in range(1, len(a)):
        current = a[i]
        j = i
        while j > 0:
            # Fehler lag im <= statt < Operator
            if key(a[j - 1]) <= key(current):
                break
            else:
                a[j] = a[j - 1]
            j -= 1
        a[j] = current


def bucketSort(a, bucketMap, d):
    N = len(a)
    M = int(N / float(d))

    buckets = [[] for k in range(M)]

    for k in range(N):
        index = bucketMap(a[k], M)
        buckets[index].append(a[k])

    start = 0
    for k in range(M):
        insertionSort(buckets[k])
        end = start + len(buckets[k])
        a[start:end] = buckets[k]
        start += len(buckets[k])

class TestSorting(unittest.TestCase):

    def setUp(self):
        self.a = createData(random.randint(10, 100))
        self.b = createData(random.randint(100, 1000))
        self.c = createData(random.randint(1000, 10000))
        self.a_sorted = copy.deepcopy(self.a)
        self.b_sorted = copy.deepcopy(self.b)
        self.c_sorted = copy.deepcopy(self.c)
        self.a_sorted_lin = copy.deepcopy(self.a)
        self.b_sorted_lin = copy.deepcopy(self.b)
        self.c_sorted_lin = copy.deepcopy(self.c)

        d = 7
        bucketSort(self.a_sorted, bucketMap, d)
        bucketSort(self.b_sorted, bucketMap, d)
        bucketSort(self.c_sorted, bucketMap, d)

        bucketSort(self.a_sorted_lin, bucketMaplin, d)
        bucketSort(self.b_sorted_lin, bucketMaplin, d)
        bucketSort(self.c_sorted_lin, bucketMaplin, d)

    def testBucketSort(self):
        self.checkIntegerSorting(self.a, self.a_sorted)
        self.checkIntegerSorting(self.b, self.b_sorted)
        self.checkIntegerSorting(self.c, self.c_sorted)

    def testBucketSortlin(self):
        self.checkIntegerSorting(self.a, self.a_sorted_lin)
        self.checkIntegerSorting(self.b, self.b_sorted_lin)
        self.checkIntegerSorting(self.c, self.c_sorted_lin)


    def checkIntegerSorting(self, original, result):
        '''Parameter 'original' contains the array before sorting,
        parameter 'result' contains the result of the sorting algorithm.'''

        #Check length
        self.assertEqual(len(original), len(result), 'Err_Int: Size is not equal')

        #Check correct elements
        result_check = copy.deepcopy(result)
        isOK = True
        for elem in original:
            try:
                result_check.remove(elem)
            except ValueError:
                isOK = False
        self.assertTrue(isOK, 'Err_Int: result does not contain same values')

        #Check order
        isOK = True
        for i in range(len(result) - 1):
            if result[i] > result[i+1]:
                isOK = False
                break
        self.assertTrue(isOK, 'Err_Int: result is not in order')


def task_2c():
    unittest.main()




if __name__ == '__main__':
    task_2b()
    task_2c()
