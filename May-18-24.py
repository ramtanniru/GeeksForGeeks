class Solution:
	def findPeakElement(self, a):
		if a[-1]>a[-2]:
			return a[-1]
		i = len(a)-1
		while a[i]<a[i-1]:
			i -= 1
		return a[i]