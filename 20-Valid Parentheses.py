class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d={']':'[','}':'{',')':'('}
        for i in s:
            if i in d.values():
                stack.append(i)
            elif stack and stack[-1]==d[i]:
                stack.pop()
            else:
                return False
        return stack == []
