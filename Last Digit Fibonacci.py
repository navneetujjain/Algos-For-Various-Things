#This program is for printing last digit of any fibonacci number(usually a little larger one).
n=int(input())
n=n%60
if n%60!=0:
    a=[1,1]
    for i in range(2,n):
        b=a[i-1]+a[i-2]
        a.append(b)
    c=a[n-1]
    d=str(c)
    k=len(d)
    print(d[k-1])
else:
    print(0)
