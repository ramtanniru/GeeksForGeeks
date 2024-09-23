class Solution:
    def findTwoElement( self,arr): 
        s = set(arr)
        n = len(arr)
        arrSum = sum(arr)
        setSum = sum(list(s))
        actualSum = (n*(n+1))//2
        return [arrSum-setSum,actualSum-setSum] 
    