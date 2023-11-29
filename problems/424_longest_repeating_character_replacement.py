from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_count = defaultdict(int)

        l = result = most_freq = 0
        for r, char in enumerate(s):
            # count the new char
            freq_count[char] += 1

            most_freq = max(most_freq, freq_count[char])
            # getting number of chars different from the most frequent char
            to_change = r - l + 1 - most_freq

            # if the quantity of chars to be changed is greater or equal to k
            if to_change > k:
                # removing the count of the last item in the window
                freq_count[s[l]] -= 1
                # reducing the window from the left
                l += 1

            # calculating the number of total chars
            result = max(result, r - l + 1)

        return max(result, r - l + 1)
