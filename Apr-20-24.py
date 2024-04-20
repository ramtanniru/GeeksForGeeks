class Solution:
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,arr1,arr2,n,m):
        arr1.extend(arr2)
        return sorted(list(set(arr1)))