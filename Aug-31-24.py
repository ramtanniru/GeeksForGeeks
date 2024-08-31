class Solution:
    def find3Numbers(self, arr):
        left = [arr[0]]
        right = [arr[-1]]
        for i in arr[::-1][1:]:
            if i>right[-1]:
                right.append(i)
            else:
                right.append(right[-1])
        for i in arr[1:]:
            if i<left[-1]:
                left.append(i)
            else:
                left.append(left[-1])
        right = right[::-1]
        res = []
        for i in range(len(arr)):
            if left[i]<arr[i]<right[i]:
                res = [left[i],arr[i],right[i]]
                break
        return res 