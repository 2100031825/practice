
def num(n):
    if n==1:
        print(n)
    else:
        print(n)
        return num(n-1)
n=int(input())
res=num(n)
