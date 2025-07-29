# This script demonstrates a simple multiplication operation with proper error handling.

import logging

from typing import Optional

def multiply(a: int, b: int) -> Optional[float]:
    """
    Multiply two numbers represented as integers and handle errors gracefully.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        Optional[float]: The result of the multiplication if successful, None otherwise.
    """
    try:
        return a * b
    except ZeroDivisionError:
        logging.error('Error: Division by zero is not allowed.')
        return None

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    
    # Test multiplication
    result = multiply(10, 5)
    if result is not None:
        print(f"{result:.2f}")
    else:
        print('Multiplication could not be performed.')