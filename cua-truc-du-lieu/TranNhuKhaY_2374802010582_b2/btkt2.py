# giải thuật sắp xếp chèn:
def insertion_s(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        # di chuyen cac ptu cua arr[0..i-1], lon hon key, den 1 vi tri phia truoc vi tri hien tai
        j=i-1
        while (j>= 0 and key < arr[j]):
            arr[j+1]= arr[j]
            j -=1
        arr[j+1]= key
arr= [14,33,27,110,135,19]
insertion_s(arr)
for i in range(len(arr)):
    print('%d' % arr[i])

# giải thuật sắp xếp nổi bọt
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
arr= [14,33,27,110,135,19]
bubble_sort(arr)
print('mảng được sắp xếp là: ',arr)