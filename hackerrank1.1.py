
arr = []
n = int(input("enter thelist size"))
for  i in range(n):
    arr.append(int(input()))
print(arr)

for i in range(n):
    j = i-1
    ele =arr[i]
    while j>=0 and ele<arr[j]:
        arr[j+1]=arr[j]
        j=j-1
    arr[j+1]=ele

print(arr)

#insertion sort o(n2)