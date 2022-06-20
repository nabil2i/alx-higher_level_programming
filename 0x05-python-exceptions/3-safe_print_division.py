#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        q = a / b
    except:
        return None
    finally:
        print("Inside result: {:f}".format(q))
