a,b=input().strip().split(" ")
if int(a)>int(b):
    n=int(a)
    m=int(b)
else:
    n=int(b)
    m=int(a)
while m!=0:
    k=m
    m=n%m
    n=k
print(n)
