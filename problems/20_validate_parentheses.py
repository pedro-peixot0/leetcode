CLOSING_PAIRS = {
    ')': '(',
    '}': '{',
    ']': '['
}

class Solution:
    @staticmethod
    def isValid(s: str) -> bool:
        open_parentheses_array = []

        for char in s:
            opening_match = CLOSING_PAIRS.get(char)
            if opening_match is not None: # if the current character is a closing parentheses
                if not open_parentheses_array:
                    return False
                if open_parentheses_array.pop(-1) != opening_match:
                    return False
            else: # if the current character is a opening parentheses
                open_parentheses_array.append(char)

        if open_parentheses_array:
            return False

        return True
