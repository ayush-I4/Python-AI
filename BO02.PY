'''

integer=int(input("enter a integer:"))
if integer==0:
    print("Zero")
elif integer >0:
    print("positive")
else:
    print("negative")


num=int(input("enter a num:"))
if num%2==0 and num!=0:
    print("even")
elif num==0:
    print("zero")
else:
    print("odd")


a=float(input("enter num1:"))
b=float(input("enter num2:"))

if a>b:
    print("num1 is greater")
else:
    if a==b:
        print("equal")
    else:
        print("num2 is greater")

        

age=int(input("enter your age:"))

if age>=60:
    print("senior citizen")
elif age>=20:
    print("adult")
elif age>=13:
    print("teenager")
else:
    print("child")

    

yr=int(input("enter a year:"))

if (yr%100!=0 and yr%4==0) or (yr%400==0):
    print(f"{yr} is a leap year")
else:
    print(f"{yr} is not a leap year.")
    


a=int(input("enter num1:"))
b=int(input("enter num2:"))
c=int(input("enter num3:"))

if (a==b==c):
    print("all numbers are equal.")
elif (a==b and a>c):
    print("print num1 and num2 are largest.")
elif (a==c and a>b):
    print("print num1 and num3 are largest.")

elif (b==c and b>a):
    print("print num2 and num3 are largest.")

elif (a<=c and b<=c):
    print("num3 is the largest no")
elif (a>=b and a>=c):
    print("num1 is the largest no.")
else :
    print("num2 is the largest no.")




a=int(input("enter num1:"))
b=int(input("enter num2:"))
c=int(input("enter num3:"))

if a > b: 
    a,b=b,a
if a>c:
    a,c=c,a
if b>c:
    b,c=c,b

print("in asc order:",a,b,c)




char=input("enter a char:")
char=char.lower()
if (char== "a" or char== "e" or char == "o" or char == "i" or char== "u"):
    print("it is a vowel.")
elif char.isalpha():
    print("it is a consonant.")
else :
    print("it is an invalid input.")

'''


