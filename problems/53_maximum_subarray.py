class Solution:
    @staticmethod
    def maxSubArray(nums: list[int]) -> int:
        best_sub_sum = -10000
        current_sub_sum = 0
        for v in nums:
            current_sub_sum += v

            if current_sub_sum > best_sub_sum:
                best_sub_sum = current_sub_sum

            if current_sub_sum < 0:
                current_sub_sum = 0

        return best_sub_sum
