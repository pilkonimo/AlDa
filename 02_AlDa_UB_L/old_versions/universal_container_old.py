import random
import copy


class UniversalContainer:
    def __init__(self):  # constructor for empty container
        self.capacity_ = 1
        self.data_ = [None]*self.capacity_
        self.size_ = 0

    def size(self):
        return self.size_

    def capacity(self):
        return self.capacity_

    def push(self, item):  # add item at the end
        if self.capacity_ == self.size_:
            self.data_.append(item)
            self.capacity_ += 1
        else:
            self.data_[self.size_] = item
        self.size_ += 1

    def popFirst(self):
        if self.size_ == 0:
            raise RuntimeError("popFirst() on empty container")
        first = self.data_[0]
        self.size_ -= 1
        for i in range(self.size_):
            self.data_[i] = self.data_[i+1]
        self.data_ = self.data_[:-1]
        self.capacity_ -= 1
        return first

    def popLast(self):
        if self.size_ == 0:
            raise RuntimeError("popFirst() on empty container")
        self.size_ -= 1
        last = self.data_[self.size_]
        self.data_ = self.data_[:-1]
        self.capacity_ -= 1
        return last

    def __getitem__(self, index):
        if index < 0 or index >= self.size_:
            raise RuntimeError("index out of range")
        return self.data_[index]

    def __setitem__(self, index, v):
        if index < 0 or index >= self.size_:
            raise RuntimeError("index out of range")
        self.data_[index] = v

    def first(self):
        return self.data_[0]

    def last(self):
        return self.data_[self.size_-1]


def test_push(c):
    # test push functionality via axioms (i)-(v) from the exercise sheet
    insert = random.randint(1, 1000)
    old_size = c.size()
    old_c = copy.deepcopy(c)
    c.push(insert)
    assert c.size() == old_size + 1  # (i)
    assert c.last() == insert  # (ii)
    for i in range(old_size):  # (iii)
        assert c[i] == old_c[i]
    if old_size == 0:  # (iv)
        assert insert == c.first()
    c.popLast()
    assert c.size_ == old_c.size_ and c.capacity_ == old_c.capacity_ and c.data_ == old_c.data_ # (v) ??assert c == old_c DIFFERENT MEMORY ADDRESS??


def test_set_item(c, index, value):
    # test setitem functionality via axioms (i)-(iii) from the exercise sheet
    old_size = c.size()
    old_c = copy.deepcopy(c)
    c[index] = value
    assert old_size == c.size()  # (i)
    assert c[index] == value  # (ii)
    for i in range(c.size()):  # (iii)
        if i == index: continue
        assert c[i] == old_c[i]


def test_pop_last(c):
    # test popLast functionality via axioms (i),(ii) from the exercise sheet
    old_size = c.size()
    old_c = copy.deepcopy(c)
    c.popLast()
    assert old_size-1 == c.size()  # (i)
    for i in range(c.size()):  # (ii)
        assert c[i] == old_c[i]


def test_pop_first(c):
    # test popFirst functionality via axioms (i),(ii) from the exercise sheet
    old_size = c.size()
    old_c = copy.deepcopy(c)
    c.popFirst()
    assert old_size-1 == c.size()  # (i)
    for i in range(c.size()):  # (ii)
        assert c[i] == old_c[i+1]


def test_first_and_last(c):
    if c.size() != 0:
        assert c.first() == c[0]
        assert c.last() == c[c.size()-1]


def test_size_capacity(c):
    assert c.size() <= c.capacity()


def constant_tests(c):
    test_size_capacity(c)
    test_first_and_last(c)


def fill_container(c):
    for i in range(0, 5):  #random.randint(0, 5)):
        c.push(random.randint(1, 1000))


def testContainer():
    c = UniversalContainer()
    # new container has size 0
    assert c.size() == 0
    # needs to hold at every time
    constant_tests(c)
    fill_container(c)
    constant_tests(c)
    test_push(c)
    constant_tests(c)
    test_set_item(c, random.randint(0, c.size()-1), random.randint(1, 1000))
    constant_tests(c)
    test_pop_last(c)
    constant_tests(c)
    test_pop_first(c)
    constant_tests(c)


testContainer()
