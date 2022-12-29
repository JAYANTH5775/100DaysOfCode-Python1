#substing
# value = True
# s = input("enter the string")
# s1 = input("enter the substring to find")
# value = (s1 in s)
# if value == True:
#     print("the entered string is substring")
# if value == False:
#     print("the entred substring is not the string")
# dict = {}
# while True:
#     student = input("enter the student name ")
#     score = input("enter the student score")
#     dict[student] = score
#     value = input("do ypu want to enter one more student(y/n)")
#     if value == 'n':
#         break
# print()
# print(len(dict))
#
# for i in range(len(dict)):
#     if dict[student] == 80 or 100:
#         print("exelent students are" + str(student))
#         if dict[student] == 70 or 85:
#             print("distinction students are" + str(student))
#         if dict[student] == 50 or 60:
#             print("poor students are" + str(student))
#         value = input("do ypu want to enter one more student(y/n)")
#         if value == 'n':
#             break


# s1 = input("enter the string 1")
# s2 = input("enter the string 2")
# while True:
#     print("enter the choice \n 1)concenate the string 2)compare the strings \n 3) exit")
#     # choice = int(input())
#
#
#     match choice:
#         case 1:
#             print("the contenation of the two strings is " + str(s1 + s2))
#         case 2:
#             print("the comaprision of the two strings is ")
#             if s1 == s2:
#                 print("the string are equal")
#             else:
#                 print("the strings arae not equal")
#         case 3:
#             break
#
#
#
# #
# s = input("enter the string")
#
# for i in range(6):
#     print(s[-1 - i])
#
# print("the stings in revers eorder")

#sum of the add number , mutiplication of the even number
# sum = 0
# mul = 1
# i=1
# n = int(input("enter the number range till u want to find the \n sum of the add number , mutiplication of the even number"))
# for i in range(n):
#     if i%2==0:
#         mul*=i
#     else:
#         sum+=i
# print("sum :" +str(sum))
# print("smultiplication is "+str(mul))

#

import re

input_string = input()
sub_string = input()

ree = re.compile(r'\s+substring\s+')
mo = ree.search(input_string)
print(mo.group())
