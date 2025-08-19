# This script demonstrates a simple multiplication operation.

import logging

from utils import divide

if __name__ == '__main__':
    # Initialize logging with a basic config
    logging.basicConfig(level=logging.INFO)
    
    # Test multiplication with floating point numbers
    result = divide(10.0, 5)
    logging.info(f"Multiplication result: {result:.2f}")
