class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l, r = 0, len(numbers) - 1

        while True:
            result = numbers[l] + numbers[r]

            if result > target:
                r -= 1
            elif result < target:
                l += 1
            else:
                return[l+1, r+1]