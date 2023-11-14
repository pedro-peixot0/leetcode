class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        set_found = set()

        for num in nums:
            if num in set_found:
                return True
            
            set_found.add(num)
            
        return False