from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in nums:
            if i in seen:
                return True
            else:
                seen.add(i)
        return False

sol = Solution()

print(sol.hasDuplicate(nums=[1, 2, 3, 3]))
print(sol.hasDuplicate(nums=[1, 2, 3, 4]))