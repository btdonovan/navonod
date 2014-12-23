#! /usr/bin/python
'''
Some programming contest problems are really tricky: not only do they
require a different output format from what you might have expected, but
also the sample output does not show the difference. For an example,
let us look at permutations.
A permutation of the integers 1 to n is an
ordering of
these integers. So the natural way to represent a permutation is
to list the integers in this order. With n = 5, a
permutation might look like 2, 3, 4, 5, 1.
However, there is another possibility of representing a permutation:
You create a list of numbers where the i-th number is the
position of the integer i in the permutation.
Let us call this second
possibility an inverse permutation. The inverse permutation
for the sequence above is 5, 1, 2, 3, 4.

An ambiguous permutation is a permutation which cannot be
distinguished from its inverse permutation. The permutation 1, 4, 3, 2
for example is ambiguous, because its inverse permutation is the same.
To get rid of such annoying sample test cases, you have to write a
program which detects if a given permutation is ambiguous or not.
Input Specification

The input contains several test cases.
The first line of each test case contains an integer n
(1 ≤ n ≤ 100000).
Then a permutation of the integers 1 to n follows
in the next line. There is exactly one space character
between consecutive integers.
You can assume that every integer between 1 and n
appears exactly once in the permutation.

The last test case is followed by a zero.
Output Specification

For each test case output whether the permutation is ambiguous or not.
Adhere to the format shown in the sample output.
Sample Input

4
1 4 3 2
5
2 3 4 5 1
1
1
0

Sample Output

ambiguous
not ambiguous
ambiguous
'''
# Understanding the concept of inverse permutations was the tricky part.
# for permutation [3, 6, 2, 1, 4, 5], 1 is in the fourth position, so the first position of the inverse permutation will be 4. 2 is in the third position so the 2nd position of the inverse permutation will be 3.
# The input specification said that the last line of input would be a zero and that the test cases would be 1 <= n <= 100000 so I set the program in a while loop that would break if n == 0. This also allows n to be set within the loop. 
# The second line of input inside the loop is the input permutation. This all happens on the 'p =' line.
# First, convert the input string into a list of ints. (list(map(int, input().split)))
# Next, enumerate that list to get position values. We want our position values to start at one. list(enumerate(list(map(int, input().split())), start=1))
# Finally, we have a list of tuples, but tuples are immutable. Convert the tuples to lists. [list(i) for i in list(...)] Our input of [3, 6, 2, 1, 4, 5] is now in the form [[1, 3], [2, 6], [3, 2], [4, 1], [5, 4], [6, 5]] The first item in each sub item is its position number (index + 1) and the second item is the original input number. The inverse list swaps position number and number.
# Now p is a list of lists and we can transform it into the inverse permutation.
# inv will be our inverse permutation. To get our inverse permutation, invert the lists in p and sort the resulting list of lists. The position numbers move to index 1 and the numbers move to index 0. The sub lists are reordered based on the number now in index 0.
# if p and inv are equivalent than the permutation is ambiguous. If they are not then they are not. :P

while True:
    n = int(input())
    if n == 0:
        break
    p = [list(i) for i in list(enumerate(list(map(int, input().split())), start=1))]
    inv = sorted([i[::-1] for i in p])
    if p == inv:
        print('ambiguous')
    else:
        print('not ambiguous')
