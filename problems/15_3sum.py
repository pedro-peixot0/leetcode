class Solution:
    @staticmethod
    def threeSum(nums: list[int]) -> list[list[int]]:
        nums.sort()
        nums_size = len(nums)

        results = []
        for idx, num in enumerate(nums):
            # stopping when reaching positives 
            # because it will be impossible to sum 0
            if num > 0:
                break

            # avoid starting with repeated numbers
            if idx > 0 and num == nums[idx-1]:
                continue
            
            # looping over the numbers ahead
            # using the same 2 pointers solution for 2 sum
            l, r = idx + 1, nums_size - 1
            while l < r:
                two_sum = nums[l] + nums[r]

                if two_sum < -num: 
                    l += 1
                elif two_sum > -num:
                    r -= 1
                else:
                    results.append([num, nums[l], nums[r]])
                   
                    l +=1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

        return results
