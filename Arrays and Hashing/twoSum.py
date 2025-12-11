from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            difference = target - nums[i]
            if difference in seen:
                return [seen[difference], i]
            seen[num] = i
           

sol = Solution()
print(sol.twoSum(nums=[3,4,5,6], target=7))
print(sol.twoSum(nums=[4,5,6], target=10))
print(sol.twoSum(nums=[5,5], target=10))