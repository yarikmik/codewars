"""
The goal of this exercise is to convert a string to a new string where each character
in the new string is "(" if that character appears only once in the original string, or ")"
if that character appears more than once in the original string.
Ignore capitalization when determining if a character is a duplicate.
"""


def duplicate_encode(word):
    new_word = ''
    if str(word).count(')') + str(word).count('(') == len(str(word)):
        return str(word)
    else:
        for symbol in str(word).lower():
            if str(word).lower().count(symbol) > 1:
                new_word += ')'
            else:
                new_word += '('
        return new_word


# print(duplicate_encode('(()))())())()'))
