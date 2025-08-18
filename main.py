# This script demonstrates a simple multiplication operation.

import logging
from typing import Optional

def multiply(a: int, b: int) -> Optional[float]:
    """
    Multiply two numbers represented as integers.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        Optional[float]: The result of the multiplication.
    """
    return a / b

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    
    # Test multiplication
    result = multiply(10, 5)
    if result is not None:
        print(f"{result:.2f}")
    else:
        print('Multiplication could not be performed.')