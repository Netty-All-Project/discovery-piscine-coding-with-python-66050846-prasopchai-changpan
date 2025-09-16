import numpy as np
array = np.array([2, 8, 9, 48, 8, 22, -12, 2])
print(f"Original array: {array}")

for i in range(len(array)):
    if array[i] > 5:
        array[i] = array[i] + array[0]

print(array)