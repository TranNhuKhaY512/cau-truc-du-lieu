# insertion sort:
def insertion_s(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        # di chuyen cac ptu cua arr[0..i-1], lon hon key, den 1 vi tri phia truoc vi tri hien tai
        j=i-1
        while (j>= 0 and key < arr[j]):
            arr[j+1]= arr[j]
            j -=1
        arr[j+1]= key
arr= [12, 31, 130, 15, 18, 150, 30]
insertion_s(arr)
print('mảng được sắp xếp là: ')
for i in range(len(arr)):
    print('%d' % arr[i])

