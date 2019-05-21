import copy
import timeit



class UniversalContainer:
    """Base Class with standard container methods"""
    def __init__(self):  # constructor for empty container
        self.capacity_ = 1
        self.data_ = [None]*self.capacity_
        self.size_ = 0

    def size(self):
        return self.size_

    def capacity(self):
        return self.capacity_

    def push(self, item):
        pass

    def popFirst(self):
        if self.size_ == 0:
            raise RuntimeError("popFirst() on empty container")
        first = self.first()
        self.size_ -= 1
        for i in range(self.size_):
            self.data_[i] = self.data_[i + 1]
        return first

    def popLast(self):
        if self.size_ == 0:
            raise RuntimeError("popLast() on empty container")
        last = self.last()
        self.size_ -= 1
        return last

    def __getitem__(self, index):  # __getitem__ implements v = c[index]
        if index < 0 or index >= self.size_:
            raise RuntimeError("index out of range")
        return self.data_[index]

    def __setitem__(self, index, v):  # __setitem__ implements c[index] = v
        if index < 0 or index >= self.size_:
            raise RuntimeError("index out of range")
        self.data_[index] = v

    def first(self):
        # alternativ auch mit self.data_[0]
        return self.__getitem__(0)

    def last(self):
        # alternativ auch mit self.data_[self.size_ -1]
        return self.__getitem__(self.size_ - 1)



class UniversalContainer1(UniversalContainer):
    """Universal container class that combines queue, array and stack functionalities."""

    def push(self, item):  # add item at the end
        if self.capacity_ == self.size_:
            self.data_.append(item)
            self.capacity_ += 1
        else:
            self.data_[self.size_] = item
        self.size_ += 1

class UniversalContainer2(UniversalContainer):
    """Universal Container that is efficient for push()"""

    def push(self, item):  # add item at the end

        if self.capacity_ == self.size_:  # internal memory is full
            self.capacity_ *= 2
            self.data_ += [None] * self.size_
        self.data_[self.size_] = item
        self.size_ += 1


class UniversalContainer3(UniversalContainer):
    """Universal Container that uses a ringpuffer as storage implementation"""
    def __init__(self): # constructor for empty container
        self.capacity_ = 1 # we reserve memory for at least one item
        self.data_ = [None]*self.capacity_ # the internal memory
        self.size_ = 0 # no item has been inserted yet
        self.in_ = 0
        self.out_ = -1

    def getindex_(self, index):
        index += self.in_
        if index <= (self.capacity() - 1):
            return index
        else:
            if self.in_ > 0:
                return index - self.capacity() + 1
            else:
                raise RuntimeError("Overflow!")

    def push(self, item): # add item at the end
        if self.capacity_ == self.size_: # internal memory is full
            self.capacity_ *= 2
            self.data_ += [None]*self.size_

            if self.out_ < self.in_:
                self.data_[0:self.size_-1] = self.data_[self.in_:self.capacity_] + self.data_[0:self.out_]
            else:
                self.data_[0:self.size_-1] = self.data_[self.in_:self.out_]

            '''if self.out_ < self.in_:
                for i in range(self.out_):
                    self.data_[self.size_ - self.in_ + i] = self.data_[i] #append ring items to the end
            for i in range(self.size_):
                self.data_[i] = self.data_[self.in_ + i]  # Shift data to beginning of array'''
            self.in_ = 0
            self.out_ = self.size_ - 1


        if self.out_ >= 0 and self.out_ < self.capacity_ - 1:
            self.out_ += 1
        elif self.out_ == self.capacity_ - 1:
            self.out_ = 0
        elif self.out_ == -1:
            self.out_ = 0
        else:
            raise RuntimeError("Something went badly wrong!")

        self.size_ += 1
        self.data_[self.out_] = item

    def popFirst(self):
        if self.size_ == 0:
            raise RuntimeError("popFirst() on empty container")
        first = self.first()
        self.size_ -= 1
        if self.in_ < self.capacity_ - 1:
            self.in_ += 1
        else:
            self.in_ = 0
        return first

    def popLast(self):
        if self.size_ == 0:
            raise RuntimeError("popLast() on empty container")
        last = self.last()
        self.size_ -= 1

        if self.out_ > 0:
            self.out_ -= 1
        else:
            self.out_ = self.capacity_ - 1
        return last

    def __getitem__(self, index): # __getitem__ implements v = c[index]
        if index < 0 or index > self.capacity_ - 1:
            raise RuntimeError("index out of range")
        return self.data_[self.getindex_(index)]

    def __setitem__(self, index, v): # __setitem__ implements c[index] = v
        if index < 0 or index > self.capacity_ - 1:
            raise RuntimeError("index out of range")
        self.data_[self.getindex_(index)] = v

    def first(self):
        return self.data_[self.in_]

    def last(self):
        return self.data_[self.out_]





def containersEqual(left, right):
    if left.size() != right.size():
        return False
    for i in range(left.size()):
        if left[i] != right[i]:
            return False
    return True

#TODO: Sinnvolle Kommentare
def testContainer(c):
    # Axiom 1
    #c = UniversalContainer()
    assert c.size() == 0
    assert c.size() <= c.capacity()

    # Axiom 3
    c.push(1)
    assert c.size() <= c.capacity()  # Axiom 2
    assert c[0] == c.first() and c[c.size() - 1] == c.last()  # Axiom 7

    assert c.size() == 1  # (i)
    assert c.last() == 1  # (ii)
    assert c.first() == 1  # (iv)
    c.popLast()  # (v)  (Container vorher leer)
    assert c.size() <= c.capacity()  # Axiom 2
    assert c.size() == 0  # (v)

    # Axiom 3 (v)
    c.push(1)
    c_old = copy.deepcopy(c)
    c.push(2)
    assert c[0] == 1  # (iii)
    c.popLast()
    assert containersEqual(c, c_old)

    # Axiom 6
    c.push(2)
    c.popFirst()
    assert c.size() == 1  # (i)
    assert c.first() == 2  # (ii)

    assert c[0] == c.first() and c[c.size() - 1] == c.last()  # Axiom 7
    assert c.size() <= c.capacity()

    # Leerer Container für folgende Tests
    c.popFirst()
    assert c.size() == 0

    # Bisschen Inhalt für folgende Tests
    c.push(2)
    c.push(3)
    c.push(4)
    c.push(5)
    assert c.size() == 4

    # Axiom 4
    for k in range(c.size()):
        c_old = copy.deepcopy(c)
        c[k] = k + 6
        assert c.size() == c_old.size()  # (i)
        for i in range(c.size()):
            if i != k:
                assert c[i] == c_old[i]  # (iii)
            else:
                assert c[i] == k + 6  # (ii)

    assert c.size() <= c.capacity()  # Axiom 2

    # Axiom 6
    c_old = copy.deepcopy(c)
    c.popFirst()
    assert c.size() == 3  # (i)
    for i in range(c.size()):  # (ii)
        assert c[i] == c_old[i + 1]

    # Axiom 5
    c_old = copy.deepcopy(c)
    c.popLast()
    assert c.size() == 2  # (i)
    for i in range(c.size()):  # (ii)
        assert c[i] == c_old[i]

    # Axiom 7
    assert c[0] == c.first() and c[c.size() - 1] == c.last()
    c.push(-1)

    cap_old = c.capacity()
    size_old = c.size()
    # Ringpuffertest
    for i in range( 2 * c.size()):
        c.popFirst()
        c.push(-1)

    assert c.capacity() == cap_old
    assert c.size() == size_old

    for i in range(c.size()):
        assert c[i] == -1

    print("All tests succeeded")


def testIt():
    c = UniversalContainer1()
    d = UniversalContainer2()
    e = UniversalContainer3()

    testContainer(c)
    testContainer(d)
    testContainer(e)

def timeIt():
    initialisation1 = '''c = UniversalContainer1()'''
    initialisation2 = '''c = UniversalContainer2()'''
    initialisation3 = '''c = UniversalContainer3()'''
    initialisation4 = '''c = []'''

    code = '''
for i in range(1000):
    c.push(i)
'''
    code4 = '''
for i in range(1000):
    c.append(i)
'''


    repeats = 100
    N = 400

    t1 = timeit.Timer(code, initialisation1, globals=globals())
    t2 = timeit.Timer(code, initialisation2, globals=globals())
    t3 = timeit.Timer(code, initialisation3, globals=globals())
    t4 = timeit.Timer(code4, initialisation4, globals=globals())
    time1 = min(t1.repeat(repeats, 1))
    time2 = min(t2.repeat(repeats, 1))
    time3 = min(t3.repeat(repeats, 1))
    time4 = min(t4.repeat(repeats, 1))

    print('execution time push c1:', (time1 * 1000), 'ms')
    print('execution time push c2:', (time2 * 1000), 'ms')
    print('execution time push c3:', (time3 * 1000), 'ms')
    print('execution time append c4:', (time4 * 1000), 'ms')

#### TESTING POPLAST:

    initialisation1 += code
    initialisation2 += code
    initialisation3 += code
    initialisation4 += code4


    code = '''
    for i in range(1000):
        c.popFirst()
    '''
    code4 = '''
    for i in range(1000):
        c.pop(0)
    '''

    repeats = 100
    N = 400

    t1 = timeit.Timer(code, initialisation1, globals=globals())
    print('check')
    t2 = timeit.Timer(code, initialisation2, globals=globals())
    print('check')
    t3 = timeit.Timer(code, initialisation3, globals=globals())
    print('check')
    t4 = timeit.Timer(code4, initialisation4, globals=globals())
    time1 = min(t1.repeat(repeats, 1))
    time2 = min(t2.repeat(repeats, 1))
    time3 = min(t3.repeat(repeats, 1))
    time4 = min(t4.repeat(repeats, 1))

    print('execution time popFirst c1:', (time1 * 1000), 'ms')
    print('execution time popFirst c2:', (time2 * 1000), 'ms')
    print('execution time popFirst c3:', (time3 * 1000), 'ms')
    print('execution time pop(0) c4:', (time4 * 1000), 'ms')


#### ERGEBNISSE
'''
(N=10000)
execution time push c1:       5.67217200000000 ms
execution time push c2:       4.39632300000003 ms
execution time push c3:      10.96485299999994 ms
execution time append c4:     0.85217400000026 ms

(N=100)
execution time popFirst c1: 168.08084199999973 ms 
execution time popFirst c2: 170.51836399999942 ms
execution time popFirst c3:   0.07445099999614 ms
execution time pop(0) c4:     0.23437699999817 ms
'''


# make universal-container.py executable
if __name__ == "__main__":
    testIt()
    timeIt()
