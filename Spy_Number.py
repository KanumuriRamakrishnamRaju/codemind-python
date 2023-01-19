n=int(input())
s=0
b=1
while n:
    m=n%10
    s=m+s
    b=m*b
    n=n//10
if s==b:
    print('Spy Number')
else:
    print('Not Spy Number')