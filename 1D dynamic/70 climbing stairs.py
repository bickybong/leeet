class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        cache = {}
        cache[1] = 1
        cache[2] = 2

        def DFS(n):
            if n in cache:
                return cache[n]
            else:
                cache[n] = DFS(n - 1) + DFS(n - 2)
                return cache[n]
        return DFS(n)
        # O(n) time n O(n) space with memoization

# can also do bottum up with fibbonacci sequence using 2 pointers
# one, two = 1, 1
#         for i in range(n-1):
#             temp = one
#             one = one + two
#             two = temp
#         return one

sol = Solution()
print(sol.climbStairs(2))
