import sys

def count_it():
    # นับจำนวน parameters (ไม่รวม sys.argv[0])
    num_params = len(sys.argv) - 1
    
    if num_params == 0:
        print("none")
    else:
        print(f"parameters: {num_params}")
        
        # แสดงแต่ละ parameter พร้อมความยาว
        for i in range(1, len(sys.argv)):
            param = sys.argv[i]
            length = len(param)
            print(f"{param}: {length}")

count_it()