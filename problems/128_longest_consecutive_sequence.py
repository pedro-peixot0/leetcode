class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        set_nums = set(nums)

        longest_sequence = 0
        for num in set_nums:
            # meaning if it is the start of a sequence
            if num - 1 not in set_nums:
                length = 1
                while num + length in set_nums:
                    length += 1
                longest_sequence = max(longest_sequence, length)

        return longest_sequence

