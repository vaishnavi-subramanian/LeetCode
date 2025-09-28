class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        if s =="":
            return False
        for c in s:
            if c.isalnum():
                res+=c.lower()
        return res == res[::-1]
