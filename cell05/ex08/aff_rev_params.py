import sys

def aff_rev_params():
    if len(sys.argv) < 3:  # ต้องมีอย่างน้อย 2 parameters
        print("none")
    else:
        # แสดง parameters ในลำดับย้อนกลับ (ไม่รวม sys.argv[0])
        for i in range(len(sys.argv) - 1, 0, -1):
            print(sys.argv[i])

aff_rev_params()