arr=[]



def binarysearch(arr, l , r ,x):
    while(r >= l):
         mid = l+(r-1)//2
         if arr[mid]==x:
             return mid
         if arr[mid]<x:
           return  binarysearch(arr,0,mid-1,x)
         if arr[mid]>x:
            return binarysearch(arr,mid+1,len(arr),x)


n = int (input())
for i in range(n):
    arr.append(int(input("enter the numbers of the list")))

print("the list elements are : "+str(arr))

key = int(input("enter the key to be searched"))
r =len(arr)
print(len(arr))
print("the key is found at "+str(binarysearch(arr,0,r,key)))


#timr o(log2n)

#merge sort o(nlogn)
#quicksort o(nlogn)