import unittest


def binarySearchI(a, key1):
    start = 0
    end = len(a)
    while (end - start) > 0:
        center = (start+end) // 2
        if key1 == a[center]:
            return center
        elif key1 < a[center]:
            end = center
        else:
            start = center + 1
    return None


class TestBinarySearch(unittest.TestCase):
    """Testclass to test binarySearch."""

    def test_basic(self):
        test_array = range(0, 99)
        self.assertEqual(binarySearchI(test_array, 50), 50)

    def test_odd_len(self):
        test_array = range(0, 100)
        self.assertEqual(binarySearchI(test_array, 45), 45)

    def test_no_key(self):
        test_array = list(range(0, 100))
        self.assertEqual(binarySearchI(test_array, 100), None)
        test_array.pop(50)
        self.assertEqual(binarySearchI(test_array, 50), None)

    def test_corner_case(self):
        test_array = range(0, 100)
        self.assertEqual(binarySearchI(test_array, 0), 0)
        self.assertEqual(binarySearchI(test_array, 99), 99)


if __name__ == '__main__':
    unittest.main()
