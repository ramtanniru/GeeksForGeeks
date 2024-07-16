class Solution:
	def printString(self, s, ch, count):
		i = 0
		while i<len(s) and count>0:
		    if s[i]==ch:
		        count -= 1
		    i += 1
		return s[i:] 