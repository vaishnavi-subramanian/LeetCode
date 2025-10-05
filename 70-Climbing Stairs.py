class Solution:
    def climbStairs(self, n: int) -> int:
        if n ==1:
            return 1
        if n == 2:
            return 2
        pre,cur = 1,2
        for i in range(2,n):
            pre,cur=cur,pre+cur
        return cur