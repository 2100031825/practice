
n=int(input())
k=[]
for i in range(2,n+1):
    for j in range(2,(i//2)+1):
        if i%j!=0:
            k.append(i)
print(k)
