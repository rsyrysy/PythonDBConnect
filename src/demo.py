"""
Demo module - Basic Python examples.

Demonstrates:
- Print statements and output formatting
- Main function pattern
- Module documentation
"""

import logging
import sys


logger = logging.getLogger(__name__)


def welcome_message() -> None:
    """
    Print welcome message to console.
    
    Demonstrates:
    - Basic print functionality
    - String output
    
    Returns:
        None
    """
    print("Hello world")
    print("Welcome to Python world")


def main() -> int:
    """
    Main entry point for demo module.
    
    Demonstrates:
    - Main function pattern
    - Return codes (0 = success)
    - Error handling
    
    Returns:
        Exit code (0 for success, 1 for failure)
    """
    try:
        logger.info("Starting demo application")
        welcome_message()
        logger.info("Demo completed successfully")
        return 0
    
    except Exception as err:
        logger.error(f"Error in demo: {err}")
        print(f"Error: {err}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
