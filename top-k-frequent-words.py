class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        if len(words) == 0:
            return []

        max_freq = 0
        count_words = {}

        for word in words:
            count_words[word] = 1 + count_words.get(word, 0)
            max_freq = max(max_freq, count_words[word])

        result = []
        freq = max_freq
        while freq >= 1:
            temp_counts = []
            for item in count_words:
                if count_words[item] == freq:
                    temp_counts.append(item)
            temp_counts.sort()
            for elem in temp_counts:
                result.append(elem)
                if len(result) == k:
                    return result
            freq -= 1