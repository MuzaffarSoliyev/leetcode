class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        min_nums = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                min_nums = min(min_nums, nums[l])
                break

            mid = (l + r) // 2
            min_nums = min(min_nums, nums[mid])
            if nums[l] <= nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return min_nums
