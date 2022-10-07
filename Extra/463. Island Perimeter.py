class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        counter = 0
        minus = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == 1:
                    counter +=1
                    if i < len(grid)-1  :
                        if grid[i+1][j]== 1:
                            minus += 1
                    if j < len(grid[i])-1 :
                        if grid[i][j+1]==1:
                            minus += 1
        return counter * 4 - minus * 2
    
        
#         check the number of land and x4 for overall perimeter
#           minus those that have land on next column, row

sol = Solution()
print(sol.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))