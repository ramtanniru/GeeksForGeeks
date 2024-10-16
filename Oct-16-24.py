class Solution:
    def checkSorted(self, arr):
        misplaced = 0
        for i,x in enumerate(arr):
            if i+1!=x:
                misplaced += 1
        cnt = 0
        for i,x in enumerate(arr):
            if cnt==2:
                break
            if i+1!=x:
                arr[x-1],arr[i] = arr[i],arr[x-1]
                cnt += 1
        for i,x in enumerate(arr):
            if i+1!=x:
                return False
        return cnt==2 or cnt==0