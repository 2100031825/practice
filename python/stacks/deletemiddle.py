#Delete middle element of a stack

# 38315

k=list(map(int,input().split()))
p=len(k)
middle=p//2

k.pop(middle)
print(k)
