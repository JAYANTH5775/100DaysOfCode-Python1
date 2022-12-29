# n = int(input())
# arr = map(int, input().split())
# print(arr)
# max = 0
# for i in range(len(arr)):
#     if arr[i] > max:
#         max = arr[i]
# for i in range(len(arr)):
#     if max - i in arr:
#         print(arr[max - i])
#         break


# n= int(input("enter the student number:"))
# student =[ ]
# for i in range(n):
#     name= input("enter the student details \n name")
#     score= int(input("enter the student score"))
#
#     student.append([name,score])
# print(student[0][0])
#
# print(student)

s = input("enter the string")
n  = len(s)
i=0
while(i<=n/2):
    if s[i] != s[n-i]:
        print("entered string is not a palindrome ")
        break
    print("entered string is a aplindrome ")
