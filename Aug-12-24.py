class Solution:
    def sum_of_middle_elements(self, arr1, arr2):
        i,j = 0,0
        mid = (len(arr1)+len(arr2))//2
        merged = []
        while i<len(arr1) and j<len(arr2) and len(merged)<=mid:
            if arr1[i]<arr2[j]:
                merged.append(arr1[i])
                i += 1
            else:
                merged.append(arr2[j])
                j += 1
        while i<len(arr1) and len(merged)<=mid:
            merged.append(arr1[i])
            i += 1
        while j<len(arr2) and len(merged)<=mid:
            merged.append(arr2[j])
        return merged[-1]+merged[-2] 