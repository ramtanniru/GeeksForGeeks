class Solution:
    def pattern (self, arr):
        # rows
        for i in range(len(arr)):
            if arr[i] == arr[i][::-1]:
                return str(i)+" R"
        # columns
        for i in range(len(arr[0])):
            x,y = 0,len(arr)-1
            while x<y:
                if arr[x][i] == arr[y][i]:
                    x += 1
                    y -= 1
                else:
                    break
            if x>=y:
                return str(i)+" C" 
        return -1 
    