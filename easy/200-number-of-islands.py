class Solution:
    def __init__(self, *args):
        def numIslands(self, grid: List[List[str]]):
            """
            :type grid: List[List[str]]
            :rtype: int
            """
            output = 0

            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == '1':
                        output += 1
                        self.dfs(grid, i, j)
            return output
        
        def dfs(self, grid, i ,j):
            """
            :type grid: List[List[str]]
            :type i: int
            :type j: int
            """
            grid[i][j] = '0'
            if i-1 >=0 and grid[i-1][j] == '1':
                self.dfs(grid, i-1, j)
            if i+1<len(grid) and grid[i+1][j]=='1':
                self.dfs(grid,i+1,j)
            if j-1>=0 and grid[i][j-1]=='1':
                self.dfs(grid,i,j-1)
            if j+1<len(grid[0]) and grid[i][j+1]=='1':
                self.dfs(grid,i,j+1)

            
            
        
                    
                
               
        
        