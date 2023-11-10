from typing import Optional

class Solution:
    @staticmethod
    def twoSum(
        nums: list[int], 
        target: int
    ) -> Optional[tuple[int]]:
        num_indexes = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in num_indexes:
                return [num_indexes[complement], i]
            
            num_indexes[num] = i 

        return None
