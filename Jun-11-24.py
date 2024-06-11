class Solution:
    def maxTip(self, n : int, x : int, y : int, arr : List[int], brr : List[int]) -> int:
        tip = 0
        l = []
        for i in range(n):
            l.append([arr[i],brr[i],abs(arr[i]-brr[i])])
        li = sorted(l,reverse=True,key=lambda x:x[2])
        for i in li:
            if x==0:
                tip += i[1]
                y -= 1
            elif y==0:
                tip += i[0]
                x -= 1
            else:
                if i[0]>=i[1]:
                    tip += i[0]
                    x -= 1
                elif i[0]<i[1]:
                    tip += i[1]
                    y -= 1
        return tip
