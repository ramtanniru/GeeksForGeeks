class Solution:
    def zigZag(self, n : int, arr : List[int]) -> None:
        def swap(arr,i,j):
            arr[i],arr[j] = arr[j],arr[i]
            return
        i,j,k = 0,1,2
        while k<n:
            if arr[i]>arr[j]:
                swap(arr,i,j)
            if arr[j]<arr[k]:
                swap(arr,j,k)
            i = k
            j,k = i+1,i+2
        if j<n:
            if arr[i]>arr[j]:
                swap(arr,i,j)
        return