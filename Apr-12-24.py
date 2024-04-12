class Solution:
    def pairAndSum(self, n, arr):
        res = 0
        for i in range(0,32):
            k = 0
            for j in arr:
                if j&(1 << i):
                    k+=1
            res += (1<<i)*(k*(k-1)/2)
        return int(res)