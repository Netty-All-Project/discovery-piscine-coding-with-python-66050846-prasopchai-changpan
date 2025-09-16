import sys

def shrink(s):
    """Takes a string and displays the first eight characters."""
    return s[:8]

def enlarge(s):
    """Takes a string and appends 'Z' characters to make it eight characters long."""
    while len(s) < 8:
        s += 'Z'
    return s

if len(sys.argv) < 2:
    print("none")
else:
    for arg in sys.argv[1:]:
        if len(arg) > 8:
            print(shrink(arg))
        elif len(arg) < 8:
            print(enlarge(arg))
        else:
            print(arg)