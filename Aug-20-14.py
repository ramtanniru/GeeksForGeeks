from collections import defaultdict
class Solution:
    def minTime(self, root,target):
        return self.burn_tree(root,target) 
        
    def build_map(self,node, parent, graph):
        if node is None:
            return
        if node not in graph:
            graph[node.data] = []
            if parent is not None:
                graph[node.data].append(parent.data)
                graph[parent.data].append(node.data)
            self.build_map(node.left, node, graph)
            self.build_map(node.right, node, graph)
    
    def burn_tree(self,root, target):
        graph = defaultdict(list)
        self.build_map(root, None, graph)
        if target not in graph:
            return 0
        visited = set()
        queue = []
        queue.append(target)
        visited.add(target)
        cnt = 0
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.pop(0)
                for next in graph[node]:
                    if next in visited:
                        continue
                    visited.add(next)
                    queue.append(next)
            cnt += 1
        return cnt-1 
