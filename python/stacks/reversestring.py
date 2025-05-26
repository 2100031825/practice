# Reverse a string using stacks 
n=input() # "pandhi"
k=[]  # p a n d h i
p=[]
for i in n:
    k.append(i)
for i in range(len(n)):
    p.append(k.pop(-1))
print(p)
