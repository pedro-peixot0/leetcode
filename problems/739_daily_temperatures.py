class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        answer = [0] * len(temperatures)

        # keep in mind that this list should be in descending order
        not_warmed = []

        for i, t in enumerate(temperatures):
            while not_warmed and temperatures[not_warmed[-1]] < t:
                i2 = not_warmed.pop()
                answer[i2] = i - i2

            not_warmed.append(i)

        return answer
