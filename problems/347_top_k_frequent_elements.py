from collections import defaultdict

class Solution:
    @staticmethod
    def topKFrequent(nums: list[int], k: int) -> list[int]:
        # getting frequency count
        dict_count = defaultdict(int)

        for num in nums:
            dict_count[num] += 1
        
        # a list of where the index represents the frequency
        length_nums = len(nums)
        freq = [[] for i in range(length_nums + 1)]
        for idx, val in dict_count.items():
            freq[val].append(idx)

        # iterating through the frequecy list from the most 
        # frequent to the least
        result = []
        for idx in range(length_nums, 0, -1):
            for val in freq[idx]:
                result.append(val)
                if len(result) == k:
                    return result


# class Solution:
#     @staticmethod
#     def topKFrequent(nums: list[int], k: int) -> list[int]:
#         # getting frequency count
#         dict_count = defaultdict(int)

#         for num in nums:
#             dict_count[num] += 1

#         return sorted(dict_count, key=dict_count.get, reverse=True)[:k]
