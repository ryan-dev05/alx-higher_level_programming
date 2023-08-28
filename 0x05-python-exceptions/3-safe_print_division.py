#!/usr/bin/python3

def safe_print_division(a, b):
    """Returns the result of base raised to the power of exponent."""
    try:
        result = a/b
    except (TypeError, ValueError):
        result = None
    finally:
        print("Inside result: {}".format(result))
    return (result)
