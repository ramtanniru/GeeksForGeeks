from collections import deque

class Solution:
    def rotateDelete(self,  arr):
        queue = deque(arr)
        k = 1
        while len(queue)>2:
            temp = queue.pop()
            queue.appendleft(temp)
            if k<=len(queue):
                del queue[-k]
            else:
                queue.popleft()
            k += 1
        return queue[0] 