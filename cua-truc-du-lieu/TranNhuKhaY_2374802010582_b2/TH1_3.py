# bubble_sort:
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) -i -1):
            temp= arr[j]
            arr[j]= arr[j+1]
            arr[j+1]= temp
arr=[25,17,7,14,6,3,100,-2,-10,-50]
print('mang chua duoc sap xep la: ', arr)
bubble_sort(arr)
print('mang duoc sap xep la: ', arr)
