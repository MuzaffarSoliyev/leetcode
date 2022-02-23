class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = {}
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in hash_map:
                return [hash_map[diff], idx]
            hash_map[num] = idx
