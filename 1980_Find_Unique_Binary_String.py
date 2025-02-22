class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        def all_nums(n):
            if n==1:
                return ['0','1']
            
            digits = ['0','1']
            binary_digits = all_nums(n-1)
            l = [i+j for i in digits for j in binary_digits]
            return l
        
        all_binary_nums = all_nums(len(nums))
        not_present = [i for i in all_binary_nums if i not in nums]
        if len(not_present)==0:
            return None
        return not_present[0]
