class Solution:
    def segregate0and1(self, arr):
        flag = False
        for i in range(len(arr)):
            if not flag and arr[i]==1:
                flag = True
                temp = i
            if flag:
                if arr[i]==0:
                    arr[temp],arr[i] = arr[i],arr[temp]
                    temp = temp + 1 