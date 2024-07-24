# 
def tuyen_tinh(array, n, x):
    for i in range(0, n):
        if (array[i]==x):
            return i
    return -1
array=[15,25,80,30,60,50,110,100,130, 180]
x=110
n=len(array)
result= tuyen_tinh(array, n, x)
print('phan tu tim thay tai vi tri la: ', result)
# 
def tuyen_tinh(array, n, x):
    for i in range(0, n):
        if (array[i]==x):
            return i
    return -1
array=[15,25,80,30,60,50,110,100,130, 180]
x=185
n=len(array)
result= tuyen_tinh(array, n, x)
if tuyen_tinh(array,n,x) == -1:
    print('khong tim thay vi tri')
else:
    print('phan tu tim thay tai vi tri la: ', result)