import sys

def aff_first_param():
    if len(sys.argv) > 1:
        print(sys.argv[1])
    else:
        print("none")

aff_first_param()