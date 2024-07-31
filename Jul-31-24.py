from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.d = defaultdict(TrieNode)
class Solution:
    def __init__(self):
        self.root = TrieNode()
    def insert(self,s):
        curr = self.root
        for c in s:
            if c not in curr.d:
                curr.d[c] = TrieNode()
            curr = curr.d[c]
    def insertNext(self,w,s):
        curr = self.root
        for i in range(len(w)):
            if s[i] not in curr.d:
                curr.d[s[i]] = TrieNode()
            curr = curr.d[s[i]]
    def searchLongestPrefix(self):
        curr = self.root
        res = ""
        while len(curr.d.keys())==1:
            res += list(curr.d.keys())[0]
            curr = list(curr.d.values())[0]
        return res if res else -1 
            
    def longestCommonPrefix(self, arr):
        miN,ele = float('inf'),""
        for i in arr:
            if len(i)<miN:
                miN = len(i)
                ele = i
        self.insert(ele)
        for i in arr:
            if i!=ele:
                self.insertNext(ele,i)
        return self.searchLongestPrefix() 