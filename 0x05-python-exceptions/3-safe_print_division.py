#!/usr/bin/python3

def safe_print_power(base, exponent):
    """Returns the result of base raised to the power of exponent."""
    try:
        result = base ** exponent
    except (TypeError, ValueError):
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
