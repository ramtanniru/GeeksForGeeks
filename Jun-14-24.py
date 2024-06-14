class Solution:
    def armstrongNumber (self, n):
        s = 0
        x = n
        while x>0:
            s += (x%10)**3
            x = x//10
        if s==n:
            return 'true'
        return 'false'