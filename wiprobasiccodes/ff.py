def count_primes(n):
    if n <= 1:
        return 0
    count = 0
    while n % 2 == 0:
        count += 1
        n //= 2
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            count += 1
            n //= i
    if n > 2:
        count += 1
    return count

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    
    product = 1
    for x in arr:
        primes = count_primes(x)
        product = (product * (primes + 2)) % (10**9 + 7)
        
    print(product)

t = int(input())
for _ in range(t):
    solve()