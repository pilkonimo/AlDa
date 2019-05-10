class testClass():
    def __init__(self, color):
        self.color_ = color
        self.size_ = 0
        self.data_ = [1, 2, 3]
    def increment(self):
        self.size_ += 1

    def size(self):
        return self.size_


def test_color(obj):
    assert obj.color_ == 'red', 'ney'


def test_size(obj):
    obj.increment()
    assert obj.size_ == 2, 'ney'


def test():
    t1 = testClass('red')
    t2 = testClass('red')
    # assert t1 == t2
    str = t1.color_
    # t1.color_ = 'blue'
    assert t1.color_ is str, 'is'
    assert t1.color_ == str, '=='


# test()


def array_test():
    t = testClass('green')
    old_data = t.data_
    assert old_data is t.data_, 'none'
    old_data = t.data_[:]
    assert old_data is t.data_, '[:]'


# array_test()


def recursive_test(counter):
    if counter < 10:
        counter += 1
        recursive_test(counter)
    return counter


def recursive_test_main():
    print(recursive_test(0))


recursive_test_main()
