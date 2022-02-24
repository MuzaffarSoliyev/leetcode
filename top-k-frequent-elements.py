class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = {}
        nums_freq = [[] for _ in nums]

        for num in nums:
            counts[num] = 1 + counts.get(num, 0)

        for key, val in counts.items():
            nums_freq[val - 1].append(key)

        res = []

        for i in range(len(nums_freq) - 1, -1, -1):
            for j in nums_freq[i]:
                res.append(j)
                if len(res) == k:
                    return res


if __name__ == '__main__':
    s = Solution()
    print(s.topKFrequent([1], 1))