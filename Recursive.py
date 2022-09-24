#Recurive Solutions To Various Problems

#Recursive Solution Of Fibonacci Numbers
def fibo(n):
    if n<2:
        return n
    else:
        return fibo(n-1)+fibo(n-2)
n=5
print(f"Fibonacci Answer={fibo(n)}")



#Recursive Solution of Factorial Of A Number
def facto(n):
    if n==0:
        return 1
    else:
        return n*facto(n-1)
n=5
print(f"Factorial Of A Number = {facto(n)}")



#Recursive Solution To Print Consecutive Numbers From 1 to N
def cons(k,n):
    if n==k:
        print(n)
        return n
    else:
        print(n)
        return cons(k,n+1)
k=5
n=1
cons(k,n)


#Recursive Solution for binary search
def bin(arr,target,start,end):
    middle=start+((end-start)//2)
    if arr[middle]==target:
        return target
    elif target>arr[middle] and start<=end:
        start=middle+1
        return bin(arr,target,start,end)
    elif target<arr[middle]and start<=end:
        end=middle-1
        return bin(arr,target,start,end)
    elif start>end:
        return -1
arr=[1,2,3,4,5,6,7,11,14,17,18]
target=11
start=0
end=len(arr)-1
print(f"Binary Search Result is {bin(arr,target,start,end)}.")



#Recursive Solution For Calculations Of Sum Of Digits Of Number
def digitsum(n):
    if n//10==0:
        return n%10
    else:
        return n%10 + digitsum(n//10)
n=1453678021
print(digitsum(n))



#Recursive Solution For Calculations Of Product Of Digits Of Number
def digitprod(n):
    if n//10==0:
        return n%10
    else:
        return n%10 * digitprod(n//10)
n=145367821
print(digitprod(n))



#Recursive Solution For Reversing A Number
def reverse(n,k):
    if n//10==0:
        return k+(n%10)
    else:
        k+=(n%10)
        k=k*10
        return reverse(n//10,k)
n=1234506
k=0
print(f"Reversed Number is {reverse(n,k)}")



#Recursive Solution For Palindrome
def reverse(n,k):
    if n//10==0:
        return k+(n%10)
    else:
        k+=(n%10)
        k=k*10
        return reverse(n//10,k)
n=123454321
k=0
p=reverse(n,k)
if p==n:
    print(f"Yes {n} is a palindrome.")
else:
    print(f"No {n} is not a palindrome.")



#Recursive Solution To Count Number Of Zeroes In A Number
def count(n):
    if n%10==0:
        return 1 + count(n//10)
    if n//10==0:
        return 0
    return count(n//10)

n=1000011001100
res=0
print(f"Number Of Zeroes Is {count(n)}")



#Recursive Solution To Check If an array is Sorted or not
def sorted(arr,index):
    if index==len(arr)-1:
        return True
    
    return arr[index]<=arr[index+1] and sorted(arr,index+1)

arr=[1,2,3,4,7,6,8,11]
index=0
print(f"The Array Is Sorted :- {sorted(arr,index)}") 



#Recursive Solution For Linear Search
def linsearch(arr,target,n):
    if n==0 and arr[n]!=target:
        return False
    elif arr[n]==target:
        return True
    else:
        return linsearch(arr,target,n-1)

arr=[1,13,34,54,24,58,99,112,226,7,9,15,19]
target=1
n=len(arr)-1
x=linsearch(arr,target,n)
if x==True:
    print(f"{target} is in the array")
else:
    print(f"{target} is not in the array")



#Recursive Solution For Linear Search Of Multiple Occurences
def linmul(arr,target,p,n):
    if arr[n]==target:
        p.append(n)
        if n==0:
            return
        else:
            return linmul(arr,target,p,n-1)
    if n==0:
        return
    else:
        return linmul(arr,target,p,n-1)

arr=[1,13,34,99,1,54,24,58,1,99,112,1,226,99,7,9,15,99,19]
target=1
n=len(arr)-1
p=[]
linmul(arr,target,p,n)
if len(p)>=1:
    print(f"{target} is in the array with the indices {p}")
else:
    print(f"{target} is not in the array")
