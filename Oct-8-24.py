class Solution:
    def pairsum(self, arr : List[int]) -> int:
        a,b = 0,0
        for i in arr:
            if i>a:
                b = max(a,b)
                a = i
            elif i>b:
                b = i
        return a+b 