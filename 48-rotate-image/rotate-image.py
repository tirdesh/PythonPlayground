class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        for i in range(n):
            p,q=0,n-1
            while p<q:
                matrix[i][p],matrix[i][q] = matrix[i][q],matrix[i][p]
                p+=1
                q-=1
        