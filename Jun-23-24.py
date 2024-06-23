class Solution:
	def bracketNumbers(self, s):
	    res = []
	    stk = []
	    op = 1
	    for i in s:
	        if i=='(':
	            res.append(op)
	            stk.append(op)
	            op += 1
	        elif i==')':
	            res.append(stk[-1])
	            stk.pop()
	    return res 