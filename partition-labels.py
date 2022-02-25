class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        last_index = {}
        for i, c in enumerate(s):
            last_index[c] = i

        size, end = 0, 0
        result = []
        for i, c in enumerate(s):
            size += 1
            end = max(last_index[c], end)
            if end == i:
                result.append(size)
                size = 0
        return result
