class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        all_stacks = []

        def recursive_parenthesis(string, open_count, closed_count):
            if len(string) == 2*n:
                all_stacks.append(string)
                return
            if open_count > closed_count:
                recursive_parenthesis(string + ')', open_count, closed_count + 1)
            if open_count < n:
                recursive_parenthesis(string + '(', open_count + 1, closed_count)

        recursive_parenthesis('', 0, 0)
        return all_stacks
