
n=int(input())
k=n
sum=0
for i in range(1,(n//2)+1):
    if n%i==0:
        sum+=i

        

if k==sum:
    print("perfect number")
else:
    print("not a perfect number")


    
