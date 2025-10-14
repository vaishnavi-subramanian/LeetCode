class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = 0
        count = 1
        arr = list(set(nums))
        arr.sort()
        for i in range(1,len(arr)):
            if arr[i-1]+1==arr[i] :
                count+=1
            else:
                res= max(res,count)
                count =1
        res = max(res,count)
        return count