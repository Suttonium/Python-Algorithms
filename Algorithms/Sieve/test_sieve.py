from unittest import TestCase
from .Sieve import Sieve


class TestSieve(TestCase):
    def test_one(self):
        param = [2, 3, 5, 7, 11, 13, 17, 19]
        self.assertEqual(param, Sieve.sieve(20))

    def test_two(self):
        param = []
        self.assertEqual(param, Sieve.sieve(0))

    def test_three(self):
        param = []
        self.assertEqual(param, Sieve.sieve(1))

    def test_four(self):
        param = [2, 3, 5]
        self.assertEqual(param, Sieve.sieve(5))

    def test_five(self):
        param = []
        self.assertEqual(param, Sieve.sieve(1))
