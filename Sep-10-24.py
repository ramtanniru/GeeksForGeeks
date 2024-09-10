from collections import defaultdict
class Solution:
    def isCircle(self, arr):
        def dfs(node):
            if node not in vis:
                vis.add(node)
                for child in adj[node]:
                    dfs(child)
        adj = defaultdict(list)
        vis = set()
        inDegree = defaultdict(int)
        outDegree = defaultdict(int)
        for w in arr:
            u = ord(w[0])-ord('a')
            v = ord(w[-1])-ord('a')
            adj[u].append(v)
            inDegree[v] += 1
            outDegree[u] += 1

        for k in adj.keys():
            if inDegree[k]!=outDegree[k]:
                return 0
        comp = 0
        for k in adj.keys():
            if k not in vis:
                comp += 1
                dfs(k)
        return 0 if comp>1 else 1 