def prime(n):
    for i in range(2,n):
        if n%i!=0:
            return "prime"
        else:
            return "not prime"
n=int(input())
result=prime(n)
print(result)
