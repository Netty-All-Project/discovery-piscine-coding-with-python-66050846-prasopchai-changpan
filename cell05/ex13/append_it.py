import sys

def append_it():
    if len(sys.argv) == 1:  # ไม่มี parameters
        print("none")
    else:
        # วนลูปผ่านทุก parameters (ข้าม sys.argv[0])
        for i in range(1, len(sys.argv)):
            param = sys.argv[i]
            
            # ตรวจสอบว่า parameter จบด้วย "ism" หรือไม่
            if param.endswith("ism"):
                # ถ้าจบด้วย "ism" แล้ว ข้ามไป (ไม่แสดง)
                continue
            else:
                # ถ้าไม่จบด้วย "ism" ให้เพิ่ม "ism" ต่อท้าย
                print(param + "ism")

append_it()