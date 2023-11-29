class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        left = 0
        max_length = 0
        for char_idx, char in enumerate(s):
            if char in seen:
                
                max_length = max(max_length, char_idx-left)

                if seen[char] < left:
                    max_length = max(max_length, char_idx-left + 1)
                else:
                    left = seen[char] + 1
            seen[char] = char_idx

        return max(max_length, char_idx-left)
    
# Second solution
# class Solution:
#     @staticmethod
#     def lengthOfLongestSubstring(s: str) -> int:
#         max_size = start_index = end_index = 0
#         for i, c in enumerate(s):
#             if c in s[start_index:end_index]:
#                 sub_length = end_index - start_index
                
#                 max_size = sub_length if sub_length > max_size else max_size

#                 start_index = s[start_index:end_index].index(c) + start_index + 1
            
#             end_index = i + 1
            
#         return max(max_size,end_index - start_index)