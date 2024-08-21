import heapq
from collections import defaultdict
class Solution:
    def shortestPath(self, edges, n, m, src):
        dist = [float('inf') for i in range(n)]
        adj = defaultdict(list)
        for s,d in edges:
            adj[s].append(d)
            adj[d].append(s)
        dist[src] = 0
        minHeap = []
        minHeap.append((src,0))
        while minHeap:
            node,c = heapq.heappop(minHeap)
            for child in adj[node]:
                if dist[child]>c+1:
                    dist[child] = c+1
                    heapq.heappush(minHeap,(child,c+1))
        for i in range(n):
            if dist[i]==float('inf'):
                dist[i] = -1
        return dist 