class Solution:
    @staticmethod
    def lengthOfLongestSubstring(s: str) -> int:
        max_size = 0
        substring = []
        for c in s:
            if c in substring:
                sub_length = len(substring)
                max_size = sub_length if sub_length > max_size else max_size
                substring = substring[substring.index(c)+1:]                

            substring.append(c)
        

        return max(max_size,len(substring))
    
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