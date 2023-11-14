class Solution:
    @staticmethod
    def findClosestElements(arr: list[int], k: int, x: int) -> list[int]:
        return sorted(sorted(arr, key = lambda v: abs(v-x))[:k])