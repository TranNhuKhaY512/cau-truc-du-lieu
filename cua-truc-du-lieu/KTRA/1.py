# a) Áp dụng giải thuật tìm kiếm nhị phân. Mảng sắp xếp tăng dần. Dãy số gồm 8 phần tử và x=55= key
# [2, 4, 12, 17, 24, 31, 40, 50]
def binary_search(arr, left, right, key): 
    if (right >= left):
        mid = (left + right) // 2
        if (arr[mid]== key):
            return mid
        elif (arr[mid]> key):
            return binary_search(arr, left, mid -1,key)
        else:
            return binary_search(arr, mid +1 , right, key)
    else:
        return -1
arr= [2, 4, 12, 17, 24, 31, 40, 50]
key = 55
result = binary_search(arr, 0, len(arr) -1, key)
if (result != -1):
    print('vi tri tim thay thu i la: ', str(result))
else:
    print(f'khong tim thay phan tu {key} trong mang')
    
# b) Áp dụng giải thuật sắp xếp nổi bot: [55, 42, 26, 10]
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
arr= [55, 42, 26, 10]
bubble_sort(arr)
print('mảng được sắp xếp là: ',arr)
