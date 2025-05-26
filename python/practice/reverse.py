# Input: arr[] = {1, 4, 3, 2, 6, 5}  
# Output: {5, 6, 2, 3, 4, 1}

a=[1,4,3,2,6,5]
k=[]
for i in range(len(a)):
    k.append(a[-1])
    a.pop(-1)
print(k)

