def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        result = 0
        for i in range(n):
            for j in range(n):
                if i == j:
                    result += mat[i][j]      
                if i + j == n-1 and i != j:
                    result += mat[i][j]             
        return result
        
