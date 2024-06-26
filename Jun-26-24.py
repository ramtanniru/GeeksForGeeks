class Solution:
	def findCoverage(self, matrix):
		cnt = 0
		for i in range(len(matrix)):
		    for j in range(len(matrix[0])):
		      if matrix[i][j]==0:
		        if i>0:
		            cnt += 1 if matrix[i-1][j]==1 else 0
		        if j>0:
		            cnt += 1 if matrix[i][j-1]==1 else 0
		        if i<len(matrix)-1:
		            cnt += 1 if matrix[i+1][j]==1 else 0
		        if j<len(matrix[0])-1:
		            cnt += 1 if matrix[i][j+1]==1 else 0
		return cnt 