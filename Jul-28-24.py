class Solution:
	def removeDups(self, str):
		alphabets = [0]*26
		for i in str:
		    alphabets[ord(i)-ord('a')] += 1
		res = ""
		for i in str:
		    if alphabets[ord(i)-ord('a')]>0:
		        res += i
		    alphabets[ord(i)-ord('a')] = 0
		return res 