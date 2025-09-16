import sys

def free_range():
    if len(sys.argv) != 3:  # ต้องมี parameters ครบ 2 ตัว
        print("none")
    else:
        try:
            # แปลง parameters เป็นตัวเลข
            start = int(sys.argv[1])
            end = int(sys.argv[2])
            
            # สร้าง array โดยใช้ range function
            result = list(range(start, end))
            
            # แสดงผลลัพธ์
            print(result)
            
        except ValueError:
            # ถ้าแปลงเป็นตัวเลขไม่ได้
            print("none")

free_range()