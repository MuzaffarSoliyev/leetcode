class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s) < len(p):
            return []

        count_s, count_p = {}, {}

        for i in range(len(p)):
            count_p[p[i]] = 1 + count_p.get(p[i], 0)
            count_s[s[i]] = 1 + count_s.get(s[i], 0)

        res = [0] if count_s == count_p else []

        l = 0

        for r in range(len(p), len(s)):
            count_s[s[r]] = 1 + count_s.get(s[r], 0)
            count_s[s[l]] -= 1

            if count_s[s[l]] == 0:
                count_s.pop(s[l])
            l += 1

            if count_s == count_p:
                res.append(l)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.findAnagrams("cbaebabacd", "abc"))
