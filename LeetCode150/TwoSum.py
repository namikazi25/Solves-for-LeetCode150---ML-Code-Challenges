from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)): 
            for j in range(len(nums)):
                if i != j:
                    if (nums[i] + nums[j]) == target:
                        return [i,j] if j > i else [j, i]
                else: 
                    pass
                
nums = [2, 7, 11, 15]
target = 9
print(Solution().twoSum(nums, target))