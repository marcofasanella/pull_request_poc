# This script demonstrates a simple multiplication operation.

import logging


def multiply(a: float, b: float) -> float:
    "/""
    Multiply two numbers represented as floating-point numbers.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The result of the multiplication, or returns an error if inputs are invalid which is currently not handled since input validation is not present.
    "/""
    return a * b

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    
    # Test multiplication with floating point numbers
    result = multiply(10.0, 5.0)
    print(f"{result:.2f}")
