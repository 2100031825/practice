
k=int(input())
n=k
rev=0
while(n>0):
    last=n%10
    n=n//10
    rev=rev*10+last

if k==rev:
    print("Palindrome")
else:
    print("Not a Palindrome")

