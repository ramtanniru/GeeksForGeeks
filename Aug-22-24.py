from collections import defaultdict,deque
from typing import List
class Solution:
    def topoSort(self,adj,V):
        inDegree = [0 for i in range(V)]
        for i,x in enumerate(adj):
            for j in x:
                inDegree[j] += 1
        queue = deque([])
        for i,x in enumerate(inDegree):
            if x==0:
                queue.append(i)
        res = []
        while queue:
            node = queue.popleft()
            res.append(node)
            for child in adj[node]:
                inDegree[child]-=1
                if inDegree[child]==0:
                    queue.append(child)
        return res
        
    def findOrder(self, alien_dict: List[str], N: int, K: int) -> str:
        adj = [[] for i in range(K)]
        
        for i in range(N-1):
            s1 = alien_dict[i]
            s2 = alien_dict[i+1]
            for j in range(min(len(s1),len(s2))):
                if s1[j]!=s2[j]:
                    adj[ord(s1[j])-ord('a')].append(ord(s2[j])-ord('a'))
                    break
        
        res = self.topoSort(adj,K)
        alpha = "abcdefghijklmnopqrstuvwxyz"
        
        for i in range(len(res)):
            res[i] = alpha[res[i]]
            
        return res 