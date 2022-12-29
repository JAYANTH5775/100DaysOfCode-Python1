
def factorial( num):
    return 1 if (num==0 or num==1 ) else num * factorial(num -1)

a = int(input("enter the number"))
b = int(input("enter the number 2"))
print ("the octal representaion is "+str(oct(a+b)))
print("the maximum of the numbers are"+str(max(a,b)))
f = factorial(a)
print("factorial odf the number is "+str(f))
p, r,t =input("enter the ,principle,rate,time").split()
summation =int(p)*int(r)*int(t)
print("the simple intrest is "+str(summation))
