import sys

def upcase_it():
    if len(sys.argv) == 2:  # ต้องมี parameter เดียวเท่านั้น
        print(sys.argv[1].upper())
    else:
        print("none")

upcase_it()