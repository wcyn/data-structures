# https://leetcode.com/problems/generate-parentheses/description/
class SolutionFaulty:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def append_left(p):
            return "()" + p

        def append_right(p):
            return p + "()"

        def enclose(p):
            return "(" + p + ")"

        def generator(pairs, parens="()", memo={}):
            if len(parens) == n*2:
                return parens

            p1 = enclose(parens)
            p2 = append_left(parens)
            p3 = append_right(parens)
            if parens not in memo:
                memo[parens] = generator(pairs, p1, memo) + " " + generator(pairs, p2, memo) + " " + generator(pairs, p3, memo)
            return memo[parens]

        result = generator(n)
        return list(set(result.split()))


sol = SolutionFaulty()
# sol.generateParenthesis(1)
print(sol.generateParenthesis(4))

class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def generate(A=[]):
            # print(A, end=" - \n")
            if len(A) == 2*n:
                if valid(A):
                    ans.append("".join(A))
            else:
                A.append('(')
                generate(A)
                A.pop()
                A.append(')')
                generate(A)
                A.pop()

        def valid(A):
            bal = 0
            for c in A:
                if c == '(': bal += 1
                else: bal -= 1
                if bal < 0: return False
            return bal == 0

        ans = []
        generate()
        return ans



sol2 = Solution()
# print(sol2.valid("()(())"))
print(sol2.generateParenthesis(4))
# sol2.generate(3)