class Solution:
	def matchPairs(self, n, nuts, bolts):
		x = set(nuts)
		order = ['!','#','$','%','&','*','?','@','^']
		idx = 0
		for i in order:
			if i in x:
				nuts[idx] = i
				bolts[idx] = i
				idx += 1
		return