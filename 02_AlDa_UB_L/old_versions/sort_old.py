import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import timeit

# functions for fitting


def fit_ins(N, a, b, c):
    return a*N**2+b*N+c


def fit_merge(N, a, b, c):
    return a*N*np.log(N)+b*N+c


def fit_quick(N, a, b, c):
    return a*N*np.log(N)+b*N+c

# sorting algorithms


def insertionSort(a):
    """Sorts given array via insertionsort."""
    N = len(a)
    counter = 0  # comparison counter

    for i in range(N):
        current = a[i]
        # find position where current is supposed to go
        j = i
        while j > 0:
            counter += 1
            if current < a[j-1]:
                a[j] = a[j-1]
            else:
                break
            j -= 1
        a[j] = current

    return a, counter


def merge(left, right, counter):
    """Merges left and right array into sorted and returned array."""
    res = []  # result initially empty
    i, j = 0, 0  # first index of left and right array and comparison counter
    while i < len(left) and j < len(right):
        counter += 1
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res += left[i:len(left)] + right[j:len(right)]
    return res, counter


def merge_sort_impl(a, counter):
    """Divides array in two parts, sorts them via recursion, merges them and returns merged array."""
    N = len(a)
    if N <= 1: return a, 0
    left = a[:int(N/2)]
    right = a[int(N/2):]
    left_sorted, counter_left = merge_sort_impl(left, counter)
    right_sorted, counter_right = merge_sort_impl(right, counter)
    return merge(left_sorted, right_sorted, counter_left + counter_right)


def mergeSort(a):
    """Invokes recursive function with correct start-parameter for mergesort algorithm."""
    return merge_sort_impl(a, 0)


def partition(a, l, r):
    """Returns correct positioned pivot-index and number of comparisons for given range of array."""
    pivot = l  # arbitrarily setting pivot to be the first element
    counter = 0
    for i in range(l+1, r+1):
        counter += 1
        if a[i] <= a[l]:  # cycle through array to find correct position for pivot
            pivot += 1
            a[i], a[pivot] = a[pivot], a[i]
    a[pivot], a[l] = a[l], a[pivot]
    return pivot, counter


def quick_sort_impl(a, l, r, counter):
    """If necessary, sets pivot, divides array at pivot and recursively sorts divided parts and returns sorted array
    and counter."""
    # counter += 1
    if l >= r:
        return a, 0
    k, comparisons_part = partition(a, l, r)
    counter += comparisons_part  # add number of comparisons to put pivot into place
    array, comparisons_left = quick_sort_impl(a, l, k-1, 0)
    array, comparisons_right = quick_sort_impl(a, k+1, r, 0)
    counter += comparisons_left + comparisons_right
    return a, counter


def quickSort(a):
    """Invokes recursive function with correct start-parameter for quicksort algorithm."""
    return quick_sort_impl(a, 0, len(a)-1, 0)


stmt_ins="""
def insertionSort(a):
    N = len(a)
    counter = 0  # comparison counter

    for i in range(N):
        current = a[i]
        # find position where current is supposed to go
        j = i
        while j > 0:
            counter += 1
            if current < a[j-1]:
                a[j] = a[j-1]
            else:
                break
            j -= 1
        a[j] = current

    return a, counter
"""


stmt_merge="""
def merge(left, right, counter):
    res = []  # result initially empty
    i, j = 0, 0  # first index of left and right array and comparison counter
    while i < len(left) and j < len(right):
        counter += 1
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res += left[i:len(left)] + right[j:len(right)]
    return res, counter


def merge_sort_impl(a, counter):
    N = len(a)
    if N <= 1: return a, 0
    left = a[:int(N/2)]
    right = a[int(N/2):]
    left_sorted, counter_left = merge_sort_impl(left, counter)
    right_sorted, counter_right = merge_sort_impl(right, counter)
    return merge(left_sorted, right_sorted, counter_left + counter_right)


def mergeSort(a):
    return merge_sort_impl(a, 0)
"""


stmt_quick="""
def partition(a, l, r):
    pivot = l  # arbitrarily setting pivot to be the first element
    counter = 0
    for i in range(l+1, r+1):
        counter += 1
        if a[i] <= a[l]:  # cycle through array to find correct position for pivot
            pivot += 1
            a[i], a[pivot] = a[pivot], a[i]
    a[pivot], a[l] = a[l], a[pivot]
    return pivot, counter



def quick_sort_impl(a, l, r, counter):
    # counter += 1
    if l >= r:
        return a, 0
    k, comparisons_part = partition(a, l, r)
    counter += comparisons_part  # add number of comparisons to put pivot into place
    array, comparisons_left = quick_sort_impl(a, l, k-1, 0)
    array, comparisons_right = quick_sort_impl(a, k+1, r, 0)
    counter += comparisons_left + comparisons_right
    return a, counter


def quickSort(a):
    return quick_sort_impl(a, 0, len(a)-1, 0)
"""


def create_plots(N_max=300):
    """Collects data to plot time and number of comparisons over length of array and saves them in folder 'figures'
    for every sorting algorithm."""
    data_counter, data_time = [list(), list(), list()], [list(), list(), list()]
    timer = [timeit.Timer(stmt_ins), timeit.Timer(stmt_merge), timeit.Timer(stmt_quick)]
    functions = [insertionSort, mergeSort, quickSort]
    fits = [fit_ins, fit_merge, fit_quick]
    function_names = ['insertionSort', 'mergeSort', 'quickSort']
    y_lim_top = [3*10**-5, 10**-4, 10**-4]

    # generate data
    for N in range(2, N_max):
        a = [random.randint(1, 1000) for i in range(N)]
        for i in range(3):
            a_copy = a[:]
            data_counter[i].append(functions[i](a_copy)[1])
            data_time[i].append(timer[i].timeit(N))

    data_x = np.linspace(2, N_max, N_max - 2)
    for i in range(3):
        data_y = np.array(data_counter[i])

        popt, pcov = curve_fit(fits[i], data_x, data_y)

        # counter plots
        plt.scatter(data_x, data_y, c='blue')
        plt.plot(data_x, fits[i](data_x, *popt), c='red', label=function_names[i] + ': a*N**2+b*N+c\na, b, c=' + str(popt))
        plt.xlabel('length of array')
        plt.ylabel('number of comparisons')
        plt.legend(loc='best')
        plt.savefig('figures/' + function_names[i] + '.png', format='PNG')
        plt.clf()
        # time plots
        plt.ylim(9 * 10 ** -7, y_lim_top[i])
        plt.scatter(data_x, data_time[i], c='blue')
        plt.xlabel('length of array')
        plt.ylabel('executiontime (' + function_names[i] + ')')
        plt.savefig('figures/' + function_names[i] + '_time.png', format='PNG')


create_plots()


def test_sort(sort_algorithm):
    """Tests whether passed algorithm suffices criteria for a sorting algorithm with randomly generated array."""
    a = [random.randint(1, 1000) for i in range(random.randint(1, 300))]
    a_copy = a[:]
    a_sorted = sort_algorithm(a_copy)[0]
    is_sorted = True

    #  same size
    if len(a) != len(a_sorted):
        is_sorted = False

    # same elements
    a_check = a[:]
    for element in a_sorted:
        a_check.remove(element)
    if len(a_check) != 0:
        is_sorted = False

    # array needs to be sorted
    for i in range(len(a_sorted)-1):
        if a_sorted[i] > a_sorted[i+1]:
            is_sorted = False

    return is_sorted


# print(test_sort(quickSort))
