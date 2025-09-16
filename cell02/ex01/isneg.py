#int(input()) เป้ณนการรับค่าจาก keyboard แล้วแปลงเป็น int
num = int(input())
if num < 0:
    print("This number is negative.")
elif num == 0:
    print("This number is zero.")
else:
    print("This number is positive or zero.")