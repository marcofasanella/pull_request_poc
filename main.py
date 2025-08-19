# This script demonstrates a simple multiplication operation.

import logging


if __name__ == '__main__':
    # Initialize logging with a basic config
    logging.basicConfig(level=logging.INFO)
    
    try:
        # Test multiplication, assuming corrected to actual intention
        result = 10.0 * 2  # Adjusted to demonstrate multiplication
        logging.info(f"Multiplication result: {result:.2f}")
    except ZeroDivisionError:
        logging.error("Attempted to divide by zero.")