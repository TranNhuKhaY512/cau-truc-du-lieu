import math
def binary_search(arr, key): #gọi tên hàm
    mid = 0  #gán biến
    left = 0  
    right = len(arr)
    step = 0
    while (left <= right):      #dùng câu đk while
        step = step +1 
        mid = (left + right) //2
        if (key == arr[mid]):   #dùng if để đặt điều kiện
            return mid
        if (key < arr[mid]):    #dùng if để đặt điều kiện
            right = mid -1
        else:
            left = mid + 1
        return - 1
arr =[0,4,5,9,13,18,24,28,29,35]
key = 40
result = binary_search(arr, key)
print('vi tri tim kiem thu  la: ', result)