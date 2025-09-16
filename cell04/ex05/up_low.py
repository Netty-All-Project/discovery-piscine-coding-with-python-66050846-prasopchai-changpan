#islower() and isupper() เป็น method ที่ใช้ตรวจสอบว่า character นั้นเป็นตัวพิมพ์เล็กหรือตัวพิมพ์ใหญ่
# result = '' เป็นก่อนสร้าง string ว่างเพื่อเก็บผลลัพธ์
str = input("Enter a string: ")
result = ''
for char in str:
    if char.islower(): 
        result += char.upper()
    elif char.isupper():
        result += char.lower()
    else:
        result += char
print(result)