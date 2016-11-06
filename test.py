import unittest

# Here's our "unit".


def IsOdd(n):
    return n % 2 == 1

# Here's our "unit tests".


class IsOddTests(unittest.TestCase):

    def testOne(self):
        self.failUnless(IsOdd(1))

    def testTwo(self):
        self.assertEqual(IsOdd(2), False)


def main():
    unittest.main(module='test_file')

if __name__ == 'test_file'
