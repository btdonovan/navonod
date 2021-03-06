#! /usr/bin/env python3

"""
Reverse Polish Notation (RPN) is a mathematical notation where every operator follows all of its operands. For instance, to add three and four, one would write "3 4 +" rather than "3 + 4". If there are multiple operations, the operator is given immediately after its second operand; so the expression written "3 − 4 + 5" would be written "3 4 − 5 +" first subtract 4 from 3, then add 5 to that.

Transform the algebraic expression with brackets into RPN form.

You can assume that for the test cases below only single letters will be used, brackets [] will not be used and each expression has only one RPN form (no expressions like a*b*c)
Input

The first line contains t, the number of test cases (less then 100).

Followed by t lines, containing an expression to be translated to RPN form, where the length of the expression is less then 400.
Output

The expressions in RPN form, one per line.

Example

Input:
3
(a+(b*c))
((a+b)*(z+x))
((a+t)*((b+(a+c))^(c+d)))

Output:
abc*+
ab+zx+*
at+bac++cd+^*
"""

def rpn(expression):
    """Given a string that is a properly formed algebraic expression and order of precedence is always given with parenthasis instead of assumed, rpn() will convert that string into its equivalent form in Reverse Polish Notation."""
    operands = 'abcdefghijklmnopqrstuvwxyz'
    operators = []
    answer = ''
    for i in expression:
        if i in operands:
            answer += i
        elif i == ')':
            answer += operators.pop()
        elif i != '(':
            operators.append(i)
    return answer

t = int(input())
for i in range(t):
    expr = input()
    print(rpn(expr))
