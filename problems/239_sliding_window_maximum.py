import collections

class Solution:
    @staticmethod
    def maxSlidingWindow(nums: list[int], k: int) -> list[int]:
        seen_numbers_idx = collections.deque()
        max_numbers_sliding_window = []

        for idx in range(len(nums)):
            # condintion to remove first number in deque if it is too old
            if seen_numbers_idx and seen_numbers_idx[0] == idx - k:
                seen_numbers_idx.popleft()

            # loop for removing numbers smaller than the current one
            while seen_numbers_idx and nums[seen_numbers_idx[-1]] < nums[idx]:
                seen_numbers_idx.pop()
        
            seen_numbers_idx.append(idx)

            if idx >= k - 1:
                max_numbers_sliding_window.append(
                    nums[seen_numbers_idx[0]]
                )
        
        return max_numbers_sliding_window