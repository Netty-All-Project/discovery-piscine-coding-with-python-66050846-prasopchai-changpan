import sys
import re

def scan_it():
    if len(sys.argv) != 3:  # ต้องมี parameters ครบ 2 ตัว
        print("none")
    else:
        keyword = sys.argv[1]  # คำที่ต้องการหา
        text = sys.argv[2]     # ข้อความที่ต้องการค้นหา
        
        # ใช้ re.findall() เพื่อนับจำนวนครั้งที่พบ
        count = len(re.findall(keyword, text))
        print(count)

scan_it()