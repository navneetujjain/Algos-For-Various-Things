import math
import numpy as np
def gcd(a,b):
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
  return n

a,b=input().strip().split(" ")
# 1. A Lot Simple One Liner Numpy Method
c=np.lcm(int(a),int(b))
print(c)
# 2. Little Mathematical Method
d = gcd(a,b)
e = (a * b) // d
print(e)
