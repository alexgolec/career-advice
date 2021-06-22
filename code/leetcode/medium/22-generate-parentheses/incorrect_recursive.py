'''
A stackless recursive implementation
'''

from typing import List

def valid_parens(length):
    if length == 1:
        yield '()'

    else:
        for paren in valid_parens(length - 1):
            yield '('  + paren + ')'
            yield '()' + paren
            yield paren + '()'


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return list(set(valid_parens(n)))


if __name__ == '__main__':
    print(Solution().generateParenthesis(8))
