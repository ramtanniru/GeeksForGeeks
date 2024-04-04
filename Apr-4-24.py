class Solution:
    #Function to find sum of all possible substrings of the given string.
    def sumSubstrings(self,s):
        res = int(s[0])
        ans = res
        for i in range(1,len(s)):
            res = ((int(s[i])*(i+1)) + (10*res)) %((10**9)+7)
            ans += res
        return ans % ((10**9)+7)
        
        
'''
1234:-

1 -> 1
2 -> 2 + 12
3 -> 3 + 23 + 123
4 -> 4 + 34 + 234 + 1234 = 4 + (30+4) + (230+4) + (1230+4) = 4*4 + 10*(3+23+123)

'''