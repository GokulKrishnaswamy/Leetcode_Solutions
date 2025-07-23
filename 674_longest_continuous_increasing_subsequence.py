class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        curr_l = 1
        max_l = 1
        for i in range(1, len(nums)):
            if nums[i]>nums[i-1]:
                curr_l +=1
                max_l = max(max_l, curr_l)
            else:
                curr_l = 1
        return max_l
