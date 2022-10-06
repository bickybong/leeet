class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # binary search
        # look at middle index and check if higher or lower than target
        # if higher continue with second half, if lower go to 1st half
        # repeat this until target is found
        # use 2 pointer for finding mid point
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return -1



sol = Solution()
print(sol.search([-1,0,3,5,9,12],9))