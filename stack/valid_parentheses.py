"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Input: s = "()"
Output: true

Input: s = "()[]{}"
Output: true

Input: s = "(]"
Output: false
"""

def is_valid(s: str) -> bool:
    closing = []
    pairs = {
        "}": "{",
        "]": "[",
        ")": "("
    }
    for char in s:
        if char == "{" or char == "(" or char == "[":
            closing.append(char)
        elif len(closing) == 0:
            return False
        else:
            closing_char = pairs.get(char, None)
            if closing_char is None or closing_char != closing.pop():
                return False
    return len(closing) == 0

assert is_valid("()")
assert is_valid("()[]{}")
assert not is_valid("(]")