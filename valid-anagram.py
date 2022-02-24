class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        hash_s, hash_t = {}, {}

        for elem in s:
            hash_s[elem] = 1 + hash_s.get(elem, 0)

        for elem in t:
            hash_t[elem] = 1 + hash_t.get(elem, 0)

        for key in hash_s:
            if hash_s[key] != hash_t.get(key, 0):
                return False
        return True