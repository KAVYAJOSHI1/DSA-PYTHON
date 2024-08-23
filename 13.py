"""
Given a string expression representing an expression of fraction addition and subtraction, return the calculation result in string format.

The final result should be an irreducible fraction. If your final result is an integer, change it to the format of a fraction that has a denominator 1. So in this case, 2 should be converted to 2/1.

 

Example 1:

Input: expression = "-1/2+1/2"
Output: "0/1"
Example 2:

Input: expression = "-1/2+1/2+1/3"
Output: "1/3"
Example 3:

Input: expression = "1/3-1/2"
Output: "-1/6"
"""
from fractions import Fraction

class Solution(object):
    def fractionAddition(self, expression):
        if expression[0] != '-':
            expression = '+' + expression
        
        fractions, i = [], 0
        
        while i < len(expression):
            sign = 1 if expression[i] == '+' else -1
            i += 1
            j = i
            while j < len(expression) and expression[j] not in "+-":
                j += 1
            
            fractions.append(sign * Fraction(expression[i:j]))
            i = j
        
        result = sum(fractions, Fraction(0, 1))
        return f"{result.numerator}/{result.denominator}"

# Example usage:
solution = Solution()
print(solution.fractionAddition("-1/2+1/2"))  # Output: "0/1"
print(solution.fractionAddition("-1/2+1/2+1/3"))  # Output: "1/3"
print(solution.fractionAddition("1/3-1/2"))  # Output: "-1/6"
