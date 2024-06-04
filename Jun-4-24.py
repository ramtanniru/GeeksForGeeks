class Solution:
	def binaryNextNumber(self, s):
		r = ""
		c = 0
		idx = 0
		while idx<len(s) and s[idx]=="0":
		    idx += 1
		if idx>=len(s):
		    return "1"
		s = s[idx:]
		for x,i in enumerate(s[::-1]):
		    if x==0:
		        y = c+int(i)+1
		    else:
		        y = c+int(i)
		    if y>1:
		        c = 1
		        r += "0"
		    elif y==1:
		        c = 0
		        r += "1"
		    else:
		        c = 0
		        r += "0"
		if c!=0:
		    r += "1"
		return r[::-1]