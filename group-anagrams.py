from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = defaultdict(list)
        for s in strs:
            counts = [0] * 26
            for elem in s:
                counts[ord(elem) - ord('a')] += 1
            res[tuple(counts)].append(s)
        return res.values()


if __name__ == '__main__':
    s = Solution()
    print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
