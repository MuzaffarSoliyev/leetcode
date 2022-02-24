class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]
        index = 0
        for i in intervals[1:]:
            if i[0] <= result[index][1]:
                if result[index][1] < i[1]:
                    result[index][1] = i[1]
            else:
                result.append(i)
                index += 1
        return result