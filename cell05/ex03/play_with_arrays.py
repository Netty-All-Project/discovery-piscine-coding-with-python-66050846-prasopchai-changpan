#import numpy as np
array = [2, 8, 9, 48, 8, 22, -12, 2]
print(f"Original array: {array}")

# First, apply the modification from previous exercise
for i in range(len(array)):
    if array[i] > 5:
        array[i] = array[i] + array[0]

# Then remove duplicates using set() to maintain the expected output format
unique_array = list(set(array))
#set จะทำการลบค่าซ้ำหรือรวมกัน
print(f"New Array: {unique_array}")