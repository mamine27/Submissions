class NumMatrix:

    def __init__(self, mat: List[List[int]]):

        n = len(mat)
        m = len(mat[0])
        self.pre = [[0 for i in range(m+1)] for j in range(n+1)]

        for i in range(n):
            for j in range(m):
                self.pre[i][j] = mat[i][j] + self.pre[i-1][j] + self.pre[i][j-1] - self.pre[i-1][j-1]

    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:

        box = self.pre[r2][c2]
        lft_box = self.pre[r2][c1-1]
        up_box = self.pre[r1-1][c2]
        overlap = self.pre[r1-1][c1-1]

        return box - lft_box - up_box + overlap
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)