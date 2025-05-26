
h=list(map(int,input().split()))
j=[]
for i in h:
    if i not in j:
        j.append(i)
print(j)