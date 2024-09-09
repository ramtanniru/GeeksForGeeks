class Solution:
    def sort012(self, arr):
        zero,one,two = 0,0,0
        for i in arr:
            if i==0:
                zero += 1
            elif i==1:
                one += 1
            else:
                two += 1
        i = 0
        while zero>0 and i<len(arr):
            arr[i] = 0
            zero -= 1
            i += 1
        while one>0 and i<len(arr):
            arr[i] = 1
            one -= 1
            i += 1
        while two>0 and i<len(arr):
            arr[i] = 2
            two -= 1
            i += 1
        return arr 