class Solution:
    def minSteps(self, d):
        ans = 0
        temp = 0
        i = 1
        while temp<d:
            temp += i
            i += 1
            ans += 1
        if temp==d:
            return ans
        if temp>d:
            if (d-temp)%2==0:
                return ans
            else:
                if (ans)%2==0:
                    return ans+1
                else:
                    return ans+2
        return ans
    