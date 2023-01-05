ble File  28 lines (24 sloc)  674 Bytes
#!/usr/bin/python3
"""This function adds two integers
and a and b are the two paramter this
function performs the operation on
"""


def add_integer(a, b=98):
    """Add two integer
    Arg:
        a = first paramter to be added
        b = second parameter to be added
    paramter b has defalut value 98
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b


if __name__ == "__main__":
    import doctest
    doctest.testmod()
