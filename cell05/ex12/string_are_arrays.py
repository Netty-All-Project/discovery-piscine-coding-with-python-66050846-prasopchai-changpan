import sys

def string_are_arrays():
    if len(sys.argv) != 2:  # ต้องมี parameter เดียวเท่านั้น
        print("none")
    else:
        string = sys.argv[1]  # สตริงที่ส่งเข้ามา
        found_z = False
        
        # วนลูปผ่านทุกตัวอักษรในสตริง
        for char in string:
            if char == 'z' or char == 'Z':
                print("z")
                found_z = True
        
        # ถ้าไม่พบ 'z' เลย ให้แสดง "none"
        if not found_z:
            print("none")

string_are_arrays()