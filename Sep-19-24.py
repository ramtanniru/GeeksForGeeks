class Solution:
    def reverseWords(self,str):
        li = str.split('.')
        return '.'.join(li[::-1]) 