from palindrome.doublebase import DoubleBasePalindrome
from random import randint
import unittest


class PalindromeTests(unittest.TestCase):

    def test_sum_One_Million_palindromes(self):
        """Sum 1 million double base palindromes"""
        palindromes = DoubleBasePalindrome()
        result = palindromes.sum_palindrome_numbers()
        self.assertEqual(872187, result)

    def test_repr_quality(self):
        """Try eval on the output of the repr to create another
        object"""
        palindromes = DoubleBasePalindrome()
        obj = eval(str(palindromes))
        self.assertEqual(palindromes, obj)

    def test_bad_instantiation(self):
        """Initialize the object with a negative number"""
        with self.assertRaises(ValueError):
            palindromes = DoubleBasePalindrome(max_number=-1)

    def test_generate_zero(self):
        """Generate the palindrome number: zero.
        This is a corner case for the algorithm"""
        palindromes = DoubleBasePalindrome(max_number=0)
        zero = next(palindromes.palindrome_numbers_generator())
        self.assertEqual(0, zero)

    def test_generate_eleven(self):
        """Generate the palindrome number: eleven.
        Correctly increment length of palindrome numbers"""
        palindromes = DoubleBasePalindrome(max_number=11)
        eleven = 0
        for x in palindromes.palindrome_numbers_generator():
            eleven = x
        self.assertEqual(11, eleven)

    def test_generate_random_palindrome_number_even_length(self):
        """Generate a palindrome number of even length."""
        palindromes = DoubleBasePalindrome()
        symmetric_part = str(randint(1, 99999))
        expected = symmetric_part + symmetric_part[::-1]
        number = palindromes.build_palindrome(symmetric_part,
                                              rtype=lambda x: str(x))
        self.assertEqual(expected, number)

    def test_generate_random_palindrome_number_odd_length(self):
        """Generate a palindrome number of odd length."""
        palindromes = DoubleBasePalindrome()
        symmetric_part = str(randint(1, 99999))
        center_part = str(randint(1, 99999))
        expected = symmetric_part + center_part + symmetric_part[::-1]
        number = palindromes.build_palindrome(symmetric_part,
                                              center=center_part,
                                              rtype=lambda x: str(x))
        self.assertEqual(expected, number)

    def test_exception_handler(self):
        """Raise desired exception"""
        palindromes = DoubleBasePalindrome(max_number=3)
        number = 4
        exc = ValueError
        with self.assertRaises(exc):
            palindromes.exception_handler(str(number), exc)

    def test_double_base_palindrome_generator(self):
        """Generate double base palindrome numbers"""
        palindromes = DoubleBasePalindrome(max_number=9009)
        res = [1, 3, 5, 7, 9, 33, 99, 313, 585, 717, 7447, 9009]
        for x, y in zip(palindromes.double_base_palindrome_generator(), res):
            self.assertEqual(x, y)
