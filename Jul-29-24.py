class Solution:
	def rowWithMax1s(self,arr):
		i,j = 0,len(arr[0])-1
		res = -1
		while i<len(arr) and j>=0:
		    if arr[i][j]==1:
		        res = i
		        j -= 1
		    else:
		        i += 1
		return res 