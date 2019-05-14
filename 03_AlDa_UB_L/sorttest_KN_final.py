import unittest
from random import randint
import copy

class Student:
    def __init__(self, name, mark):
        '''Construct new Student object with given 'name' and 'mark'.'''
        self.name = name
        self.mark = mark

    def getName(self):
        '''Access the name.'''
        return self.name

    def getMark(self):
        '''Access the mark.'''
        return self.mark

    def __repr__(self):
        '''Convert Student object to a string.'''
        return "%s: %3.1f" % (self.name, self.mark)

    def __eq__(self, other):
        '''Check if two Student objects are equal.'''
        return self.name == other.name and self.mark == other.mark

##################################################################

def insertionSort(a, key=lambda x: x):
    '''
    Sort the array 'a' in-place.

    Parameter 'key' must hold a function that, given a complicated
    object, extracts the property to be sorted by. By default, this
    is the object itself (useful to sort integers). To sort Students
    by name, for example, you would call:
        insertionSort(students, key=Student.getName)
    whereas to sort by mark, you use
        insertionSort(students, key=Student.getMark)
    This corresponds to the behavior of Python's built-in sorting functions.
    '''
    for i in range(1, len(a)):
        current = a[i]
        j = i
        while j > 0:
            #Fehler lag im <= statt < Operator
            if key(a[j-1]) <= key(current):
                break
            else:
                a[j] = a[j-1]
            j -= 1
        a[j] = current


def merge(left, right, key=lambda x: x):
    res = []
    j,i = 0,0
    while i < len(left) and j < len(right):

        if key(left[i]) <= key(right[j]):
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    #Eins von beiden Arrays ist 'leer', das andere wird ans Ende des res Arrays angefügt.
    res += left[i:len(left)] + right[j:len(right)]
    return res


def mergeSort(a, key=lambda x: x):

    N=len(a)
    if N <= 1:
        return a
    else:
        #Teilen der Listen mit Berücksichtigung ungerade Listenlänge
        if N % 2 == 0:
            left = a[0:int(N / 2)]
            right = a[int(N / 2):N]
        else:
            left = a[0:int((N-1)/2)]
            right = a[int((N-1)/2):N]

        leftSorted = mergeSort(left, key=key)
        rightSorted = mergeSort(right, key=key)

        res = merge(leftSorted, rightSorted, key=key)

        return res

##################################################################

class TestSortingFunctions(unittest.TestCase):

    def setUp(self):
        '''Create test data.'''

        # integer arrays
        self.int_arrays = [
            [],           # empty array
            [1],          # one element
            [2,1],        # two elements
            [3,2,3,1],   # the array from the exercise text
            [randint(0, 4) for k in range(10)], # 10 random ints
            [randint(0, 4) for k in range(10)]  # another 10 random ints
        ]

        # Student arrays
        self.student_arrays = [
           [Student('Adam', 1.3),
            Student('Bert', 2.0),
            Student('Elsa', 1.0),
            Student('Greg', 1.7),
            Student('Jill', 2.7),
            Student('Judy', 3.0),
            Student('Mike', 2.3),
            Student('Patt', 5.0)], # without replicated marks

           [Student('Adam', 1.3),
            Student('Bert', 2.0),
            Student('Elsa', 1.3),
            Student('Greg', 1.0),
            Student('Jill', 1.7),
            Student('Judy', 1.0),
            Student('Mike', 2.3),
            Student('Patt', 1.3)], # with replicated marks, alphabetic

           [Student('Bert', 2.0),
            Student('Mike', 2.3),
            Student('Elsa', 1.3),
            Student('Judy', 1.0),
            Student('Patt', 2.0),
            Student('Greg', 1.0),
            Student('Jill', 1.7),
            Student('Adam', 1.3)] # with replicated marks, random order
        ]

    def testBuiltinSort(self):
        # test the integer arrays
        for a in self.int_arrays:
            sorted = copy.deepcopy(a)
            sorted.sort()
            self.checkIntegerSorting(a, sorted)

        # test the Student arrays
        for a in self.student_arrays:
            sorted = copy.deepcopy(a)
            sorted.sort(key=Student.getMark)
            self.checkStudentSorting(a, sorted)

    def testInsertionSort(self):
        # test the integer arrays
        for a in self.int_arrays:
            sorted = copy.deepcopy(a)
            insertionSort(sorted)
            self.checkIntegerSorting(a, sorted)

        # test the Student arrays
        for a in self.student_arrays:
            sorted = copy.deepcopy(a)
            insertionSort(sorted, key=Student.getMark)
            self.checkStudentSorting(a, sorted)

    def testMergeSort(self):
        # test the integer arrays
        for a in self.int_arrays:
            sorted_arr = mergeSort(a)
            self.checkIntegerSorting(a, sorted_arr)

        # test the Student arrays
        for a in self.student_arrays:
            sorted_arr = mergeSort(a, key=Student.getMark)
            self.checkStudentSorting(a, sorted_arr)


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


    def checkStudentSorting(self, original, result):
        '''Parameter 'original' contains the array before sorting,
        parameter 'result' contains the result of the sorting algorithm.'''

        #Check length
        self.assertEqual(len(original), len(result), 'Err_Stud: Size not equal')

        #check correct elements
        result_check = copy.deepcopy(result)
        isOK = True
        for elem in original:
            try:
                result_check.remove(elem)
            except ValueError:
                isOK = False
        self.assertTrue(isOK, 'Err_Stud: result does not contain same values')

        #Check order
        isOK = True
        for i in range(len(result) - 1):
            if result[i].getMark() > result[i + 1].getMark():
                isOK = False
                break
        self.assertTrue(isOK, 'Err_Stud: result is not sorted')

        #Check stability
        for i in range(len(result)-1):
            if result[i].getMark() == result[i+1].getMark():
                if original.index(result[i]) >= original.index(result[i+1]):
                    isOK = False
                    break
        self.assertTrue(isOK, 'Err_Stud: algorithm not stable')


##################################################################

if __name__ == '__main__':
    unittest.main()



'''BEANTWORTUNG DER AUFGABEN'''

#Aufgabe 1a
'''Alle Funktionen, die mit test beginnen, werden von der unittest Klasse als TestCases interpretiert und entsprechend
automatisch durchlaufen. die check Funktionen sind lediglich hilfsfunktionen, auf die später in den test Methoden
zugegriffen wird.'''




