class Solution:
    def constructLinkedMatrix(self, mat):
        arr = [[Node(0) for i in range(len(mat))] for j in range(len(mat[0]))]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                arr[i][j] = Node(mat[i][j])
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i+1<len(mat):
                    arr[i][j].down = arr[i+1][j]
                if j+1<len(mat[0]):
                    arr[i][j].right = arr[i][j+1]
        return arr[0][0] 