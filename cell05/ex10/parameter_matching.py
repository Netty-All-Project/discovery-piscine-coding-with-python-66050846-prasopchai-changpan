import sys

def parameter_matching():
    if len(sys.argv) != 2:  # ต้องมี parameter เดียวเท่านั้น
        print("none")
    else:
        parameter = sys.argv[1]  # parameter ที่ส่งเข้ามา
        user_word = input("What was the parameter? ")  # ให้ผู้ใช้ใส่คำ
        
        if user_word == parameter:
            print("Good job!")
        else:
            print("Nope, sorry...")

parameter_matching()