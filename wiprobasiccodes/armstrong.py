
n=int(input())
k=n
p=len(str(n))
rev=0
sum=0
while(n>0):
    last=n%10
  
    n=n//10
    sum+=last**p
print(sum)

if k==sum:
    print("armstrong")
else:
    print("not a armstrong")
