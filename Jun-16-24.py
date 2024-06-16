class Solution:
    def getPrimes(self, n : int) -> List[int]:
        def SieveOfEratosthenes(n, isPrime): 
            isPrime[0] = isPrime[1] = False
            for i in range(2, n+1): 
                isPrime[i] = True
            p = 2
            while(p*p <= n): 
                if (isPrime[p] == True): 
                    i = p*p 
                    while(i <= n): 
                        isPrime[i] = False
                        i += p 
                p += 1

        isPrime = [0]*(n+1)
        SieveOfEratosthenes(n,isPrime)
        for i in range(n):
            if isPrime[i]:
                if isPrime[n-i]:
                    return [i,n-i]
        return [-1,-1]