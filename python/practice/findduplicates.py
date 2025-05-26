# Find duplicate elements in an array

# Input: {2 10 10 100 2 10 11 2 11 2}
# Output: {2, 10, 11}


# Input: {5, 40, 1, 40, 100000, 1, 5, 1}s
# Output: {5, 40, 1}

n=list(map(int,input().split()))
k=[] 
p=[] 
for i in n:
    if i in p:
        if i not in k:
            k.append(i)
    else:
        p.append(i)
print(k)


