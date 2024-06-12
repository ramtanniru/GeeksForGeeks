class Solution:
    def countNumberswith4(self, n : int) -> int:
        l = len(str(n))
        if n<4:
            return 0
        if 4<=n<10:
            return 1
        dp = [1]
        for i in range(1,l-1):
            dp.append((dp[-1]*10)+(10**len(dp)-dp[-1]))
        res = dp[-1]
        for i in range(10**(l-1),n+1):
            x = []
            while i>0:
                x.append(i%10)
                i = i//10
            if 4 in set(x):
                res += 1
        return res