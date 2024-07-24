'''sinh mảng ngẫu nhiên gồm N số nguyên có giá trị thuộc (-100,100)
Tìm phần tử có giá trị X trong mảng bằng 2 phương pháp ': tìm tuyến và nhị phân'''
# tuyến tính
import random
N =int(input('nhập số lượng phần từ trong mảng'))  # số lượng phần tử trong mảng
arr = [random.randint(-100, 100) for _ in range(N)]
print(arr)
def tim_ptu(arr, X):
    for i in range(len(arr)):
        if arr[i] == X:
            return i  # trả về vị trí của phần tử X
    return -1  # trả về -1 nếu không tìm thấy phần tử X
X = int(input('nhập phần từ muốn tìm X: '))
result = tim_ptu(arr, X)
if result != -1:
    print(f"Phần tử {X} được tìm thấy tại vị trí {result}")
else:
    print(f"Phần tử {X} không được tìm thấy")

 # nhị phân
import random
import math
N =int(input('nhập số lượng phần từ trong mảng'))  # số lượng phần tử trong mảng
arr = [random.randint(-100, 100) for _ in range(N)]
print(arr)
def find_binary(arr, X):
    arr.sort()  # sắp xếp mảng
    mid=0
    left=0
    right = len(arr) - 1
    step=0
    while left <= right:
        step=step+1
        mid = (left + right) // 2
        if arr[mid] == X:
            return mid  # trả về vị trí của phần tử X
        elif arr[mid] < X:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # trả về -1 nếu không tìm thấy phần tử X
X = int(input('nhập phần tử muốn tìm X: '))
result = find_binary(arr, X)
if result != -1:
    print(f"Phần tử {X} được tìm thấy tại vị trí {result}")
else:
    print(f"Phần tử {X} không được tìm thấy")