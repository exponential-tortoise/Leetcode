class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        
        m=len(matrix)
        n=len(matrix[0])
        
        dp=[[0 for i in range(n+1)] for i in range(m+1)]
        
        count=0
        
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==1:
                    dp[i+1][j+1]=min(dp[i+1][j],dp[i][j+1],dp[i][j])+1
                    count+=dp[i+1][j+1]
        
        return count
                
                
