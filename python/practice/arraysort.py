# sort the array in ascending order without using inbuilt functions

# 6 4 8 9 23 11 54 2
n=list(map(int,input().split()))
for i in range(len(n)-1):
    for j in range(len(n)-i-1):
        if n[j]>n[j+1]:
            n[j],n[j+1]=n[j+1],n[j]
print(n)


