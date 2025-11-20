class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        nums_dict= Counter(nums)
        # print(nums)
        # res = max(nums_dict.values())
        # return res
        result=[]
        for k,v in nums_dict.items():
            if v > len(nums)//2:
                return k
