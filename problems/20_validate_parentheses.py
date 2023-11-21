CLOSING_PAIRS = {
    ')': '(',
    '}': '{',
    ']': '['
}

class Solution:
    @staticmethod
    def isValid(s: str) -> bool:
        stack = []

        for parentheses in s:
            parentheses_pair = CLOSING_PAIRS.get(parentheses)

            # if it is a closing parentheses
            if parentheses_pair and len(stack):
                # get previous char
                previous_parentheses = stack.pop()

                # check if the last item in stack is a closing 
                if not parentheses_pair == previous_parentheses:
                    return False
            else:
                stack.append(parentheses)

        # if there are open parentheses
        if stack:
            return False

        return True
