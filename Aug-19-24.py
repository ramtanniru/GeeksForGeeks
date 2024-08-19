import heapq
class Solution:

    def kthSmallest(self, arr,k):
        maxHeap = []
        for i in range(k):
            heapq.heappush(maxHeap,-arr[i])
        for i in range(k,len(arr)):
            if -maxHeap[0]>arr[i]:
                heapq.heappop(maxHeap)
                heapq.heappush(maxHeap,-arr[i])
        return -maxHeap[0] 