class Solution:
	def PowMod(self, x, n, m):
		if n==0:
		    return 1
		if x==0:
		    return 0
		temp = self.PowMod(x,n//2,m)
		if n%2==0:
		    return temp*temp%m
		else:
		    return x*temp*temp%m