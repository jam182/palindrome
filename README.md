Project Euler Problem 36
========================
[Double-base palindromes](https://projecteuler.net/problem=36)
-------------------------
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic
in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeros.)

Solution
--------
One possible solution would have been to check every number between,
1 and 1.000.000 and see if they were palindrome in both bases.
However the density of the palindrome numbers is quite low and it seemed
more appropriate to find a way to generate them, so as to avoid checking,
every possible number.

The idea behind this approach is to first generates only palindrome numbers
in base 10, and then check if their binary counter part is palindrome too.
Since there cannot be leading zeros only odd number are worth double checking.

To generate palindrome numbers we really care about their length.
- Even length numbers can be built by attaching the reverse of themselves to
themselves.
- Odd length numbers should be created the same way as even length numbers,
but need to have digits that goes from zero to nine in the middle.
- One last thing to keep in mind is that parts of the number to mirror, vary
according to levels of iterations over pair of number-length (even, odd length).
An example will follow.
- Finally strings are more powerful than integers when it comes to manipulation,
so numbers are converted to string on the way in, and back to int on the way out.

|               | Even           | Odd       | Even   | Odd       | ...       |
| ------------- | --------------:| ---------:| ------:| ---------:| ---------:|
| Length Level  | 10**0          | 10**0     | 10**1  | 10**1     |           |
| Numbers       | 1\|1           | 1(0)\|1   | 10\|01 | 10(0)\|01 |           |
| Numbers       | 2\|2           | 1(1)\|1   | 11\|11 | 11(1)\|11 |           |
| Numbers       | 3\|3           | 1(2)\|1   | 12\|21 | 12(2)\|21 |           |
| Numbers       | 4\|4           | 1(3)\|1   | 13\|31 | 13(3)\|31 |           |
| Numbers       | 5\|5           | 1(4)\|1   | 14\|41 | 14(4)\|41 |           |
| Numbers       | 6\|6           | 1(5)\|1   | 15\|51 | 15(5)\|51 |           |
| Numbers       | 7\|7           | 1(6)\|1   | 16\|61 | 16(6)\|61 |           |
| Numbers       | 8\|8           | 1(7)\|1   | 17\|71 | 17(7)\|71 |           |
| Numbers       | 9\|9           | 1(8)\|1   | 18\|81 | 18(8)\|81 |           |
| Numbers       | ...            | 1(9)\|1   | 19\|91 | 19(9)\|91 |           |
| Numbers       |                | 2(0)\|2   | 20\|02 | 20(0)\|02 |           |
| Numbers       |                | ...       | ...    | ...       |           |

The first part of the number is generated by using length Level as starting point.
Numbers after \| are those mirrored. Numbers in () are those in the middle.
First one-digit numbers are actually a special case, generated in the same fashion
but stripping out the zero's.

Install
-------
Clone Repo: 
- ```git clone https://github.com/jam182/palindrome.git```
- ```cd palindrome```
- ```python setup.py install```

Example
-------
- ```python```
- ```>>> from palindrome import numbers```
- ```>>> from palindrome import doublebase```
- ```>>> a = numbers.PalindromeNumber()```
- ```>>> a```
- ```PalindromeNumber(max_number=1000000)```
- ```>>> b = doublebase.DoubleBasePalindrome()```
- ```>>> b```
- ```DoubleBasePalindrome(max_number=1000000)```
- ```>>> b.is_double_base_palindrome(1)```
- ```True```
