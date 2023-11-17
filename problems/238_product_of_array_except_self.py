class Solution:
    @staticmethod
    def productExceptSelf(nums: list[int]) -> list[int]:
        answer = [1]
        left_product = right_product = 1

        for num in nums[:-1]:
            left_product *= num
            answer.append(left_product)

        for idx in range(len(nums) - 1 , -1, -1):
            answer[idx] *= right_product
            right_product *= nums[idx]

        return answer
