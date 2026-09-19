'''

# 1
n = int(input())
for i in range(1, n + 1):
    print(i)

# 2
n = int(input())
for i in range(n, 0, -1):
    print(i)

# 3
n = int(input())
s = 0
for i in range(1, n + 1):
    s += i
print(s)

# 4
n = int(input())
for i in range(1, 11):
    print(n, 'x', i, '=', n * i)

# 5
n = int(input())
for i in range(2, n + 1, 2):
    print(i)

# 6
s = 0
while True:
    x = int(input())
    if x == 0:
        break
    s += x
print(s)

# 7
n = int(input())
c = 0
while n > 0:
    n //= 10
    c += 1
print(c)

# 8
n = int(input())
rev = 0
while n > 0:
    rev = rev * 10 + n % 10
    n //= 10
print(rev)

# 9
n = int(input())
temp = n
rev = 0
while n > 0:
    rev = rev * 10 + n % 10
    n //= 10
print("Palindrome" if temp == rev else "Not Palindrome")

# 10
n = int(input())
a, b = 0, 1
for _ in range(n):
    print(a)
    a, b = b, a + b

    
    '''
s = [None] * 3
top=-1
def push(n,x):
    if top==n-1:
      print("stack overflow")
      return
    if top is None:
      top=0
    else:
      top=top+1
    s[top]=x
    print(f"Pushed {x} at position {top}")
push(3,10)
push(3,20)
push(3,40)
push(3,50)