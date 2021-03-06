import os
import random

from typing import List, Any


class Random(random.Random):
    """Custom Random() class for the possibility of extending."""

    def randints(self, amount: int = 3,
                 a: int = 1, b: int = 100) -> List[int]:
        """Generate list of random integers.

        :param int amount: Amount of elements.
        :param int a: Minimum value of range.
        :param int b: Maximum value of range.
        :return: List of random integers.
        :rtype: list
        :raises ValueError: if amount less or equal to zero.
        """

        if amount <= 0:
            raise ValueError('Amount out of range.')

        return [self.randint(a, b)
                for _ in range(amount)]

    @staticmethod
    def urandom(*args: Any, **kwargs: Any) -> bytes:
        """Return a bytes object containing random bytes

        :return: Bytes.
        :rtype: bytes
        """
        return os.urandom(*args, **kwargs)
