class Solution:
    def threeSumClosest (self, arr, target):
        minD = float('inf')
        ele = target
        arr.sort()
        for i in range(len(arr)):
            t = target-arr[i]
            l,r = i+1,len(arr)-1
            while l<r:
                s = arr[l]+arr[r]
                if minD>=abs(t-s):
                    if minD==abs(t-s):
                        if ele<s+arr[i]:
                            ele = s+arr[i]
                    else:
                        minD = abs(t-s)
                        ele = s+arr[i]
                if s<t:
                    l += 1
                elif s>t:
                    r -= 1
                else:
                    return target
        return ele 