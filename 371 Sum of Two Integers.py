class Solution:
    def getSum(self, a: int, b: int) -> int:
        # while b!=0:
        #     temp = (a & b) << 1
        #     a = a ^ b
        #     b=temp
        # return a
        list1 = [a,b]
        return sum(list1)
