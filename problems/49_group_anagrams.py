from collections import defaultdict

class Solution:
    def groupAnagrams(self, strings: list[str]) -> list[list[str]]:
        anagrams = defaultdict(list)
        for string in strings:
            anagrams["".join(sorted(string))].append(string)

        return anagrams.values()
