Python编程规范：

针对比较简单的案例，Unittest 可以写可以不写。

```
import math
import unittest

def is_prime(n):
    """
    Determine if a number is a prime.

    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

    Parameters:
    n (int): The number to check for primality.

    Returns:
    bool: True if n is a prime number, False otherwise.

    Raises:
    ValueError: If n is less than 2.

    Examples:
    >>> is_prime(2)
    True
    >>> is_prime(4)
    False
    >>> is_prime(17)
    True
    """
    if n < 2:
        raise ValueError("n must be greater than or equal to 2.")
    if n == 2:
        return True  # 2 is the only even prime number
    if n % 2 == 0:
        return False  # Exclude other even numbers
    # Check for factors up to the square root of n
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

class TestIsPrime(unittest.TestCase):
    """Unit tests for the is_prime function."""

    def test_prime_numbers(self):
        """Test that prime numbers are correctly identified."""
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(17))
        self.assertTrue(is_prime(19))

    def test_non_prime_numbers(self):
        """Test that non-prime numbers are correctly identified."""
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(15))
        self.assertFalse(is_prime(20))

    def test_invalid_input(self):
        """Test that invalid inputs raise the appropriate exceptions."""
        with self.assertRaises(ValueError):
            is_prime(-5)
        with self.assertRaises(ValueError):
            is_prime(0)

if __name__ == '__main__':
    unittest.main()

```

