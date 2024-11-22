from typing import List  # {{ edit_1 }}
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_set = set(nums)
        if (len(nums) == len(nums_set)):
            return False
        else: 
            return True

nums = [1, 2, 3, 3]        
print(Solution().hasDuplicate(nums))