n=input()
l=[]
s=1
for i in n:
    l.append(int(i))
if int(n)%2==0:
    print(sum(l))
else:
    for i in l:
        s*=i 
    print(s)
