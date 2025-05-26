# reverse number 81259
n=input() # 81259
h=[]    # 8 1 2 5 9
k=[]    # 
for i in n:
    h.append(i)
print(h)
for j in range(len(h)): 
    k.append(h.pop(-1))
print(k)