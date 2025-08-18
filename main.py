# This script demonstrates a simple multiplication operation.

import logging
from typing import Optional

def multiply(a: float, b: float) -> Optional[float]:
    """
    Multiply two numbers represented as floating-point numbers.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        Optional[float]: The result of the multiplication, or None if inputs are invalid.
    """
    return a * b

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    
    # Test multiplication with floating point numbers
    result = multiply(10.0, 5.0)
    if result is not None:
        print(f"{result:.2f}")
    else:
        print('Multiplication could not be performed.')
