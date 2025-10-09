class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_num =nums[0]
        min_num = nums[0]
        result = nums[0]
        if not nums:
            return 0
        for i in range(1,len(nums)):
            num=nums[i]
            if num <0:
                min_num,max_num = max_num,min_num
            min_num = min(num,min_num*num)
            max_num = max(num,max_num*num)
            result = max(result,max_num)
        return result