import sys

def downcase_it():
    if len(sys.argv) == 2:  # ต้องมี parameter เดียวเท่านั้น
        print(sys.argv[1].lower())
    else:
        print("none")

downcase_it()