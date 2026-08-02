


#1.
name=input("name:")
print(f"Hello,{name}!Welcome to Python.")
#2.
a=int(input("a="))
b=int(input("b="))
print(f"Sum={a+b}\ndifference={a-b}\nProduct={a*b}\nDivision={a/b}\nFloor division={a//b}\nModulus={a%b}\nExponent={a**b}")
#3.
int=12
float=2.5
string="abcd"
Boolean=True
Complex=1+3j
print(f"{int} is of:" ,type(int))
print(f"{float} is of:" ,type(float))
print(f"{string} is of:" ,type(string))
print(f"{Boolean} is of:" ,type(Boolean))
print(f"{Complex} is of:" ,type(Complex))



#4.
object1="ball"
object2="bat"

object1,object2=object2,object1

print("object1:",object1)
print("object2:",object2)
#5.
temp=int(input("temp_in_celsius:"))
print("temp_in_fahrenheit=",temp*(9/5)+32)

#6.
l=int(input("length="))
b=int(input("breadth="))
print("Area=",l*b)
print("perimeter=",2*(l+b))

#7.
age=int(input("age:"))

age_f=float(age)
age_str=str(age)
age_bool=bool(age)
print("float:",age_f)
print("string:",age_str)
print("boolean:",age_bool)

#8.
total_seconds=int(input("seconds:"))


hours=total_seconds//3600
minutes=(total_seconds%3600)//60
seconds=((total_seconds%3600)%60)
print(f"time:{hours}h {minutes}m {seconds}s")

#9.
p=float(input("principle="))
t=float(input("time(in yrs)="))   #annually
r=float(input("rate(%)="))
print("simple interest=",(p*r*t)/100)

#10.
num1,num2,num3=map(float,input("num1:,num2:,num3:").split(","))


'''
if(num2>num1 and num3>num2):
    print("largest num is num3=",num3)
    print("smallest num is num1=",num1)
    print("avgerage=",(num1+num2+num3)/3)
elif(num2<num1 and num2>num3):
    print("largest num is num1=",num1)
    print("smallest num is num3=",num3)
    print("avgerage=",(num1+num2+num3)/3)
elif(num1<num2 and num2>num3):
    print("largest num is num2=",num2)
    print("avgerage=",(num1+num2+num3)/3)
    if (num1>num3):
        print("smallest num is",num3)
    else:
        print("smallest num is num1=",num1)

'''

# Find largest
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

# Find smallest
if num1 <= num2 and num1 <= num3:
    smallest = num1
elif num2 <= num1 and num2 <= num3:
    smallest = num2
else:
    smallest = num3

average = (num1 + num2 + num3) / 3

print(f"Largest number = {largest}")
print(f"Smallest number = {smallest}")
print(f"Average = {average}")





# Take inputs in one line
#P, R, T = map(float, input("Enter Principal, Rate(%), Time(in years): ").split(","))

# Calculate Simple Interest
#SI = (P * R * T) / 100


#print(f"Simple Interest = {SI}")