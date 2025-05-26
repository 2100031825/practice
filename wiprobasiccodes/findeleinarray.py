
n=int(input())
k=list(map(int,input().split()))
if n in k:
    print(k.index(n))
else:
    print("element is not present")
