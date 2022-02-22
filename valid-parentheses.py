class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for bracket in s:
            if bracket in {'(', '{', '['}:
                stack.append(bracket)
            if bracket in {')', '}', ']'}:
                if len(stack) > 0:
                    last = stack.pop()
                else:
                    return False
                if last == '(' and bracket == ')':
                    continue
                elif last == '{' and bracket == '}':
                    continue
                elif last == '[' and bracket == ']':
                    continue
                else:
                    return False
        return True if len(stack) == 0 else False
