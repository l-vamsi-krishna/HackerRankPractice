# https://www.hackerrank.com/challenges/capitalize/problem
# Score = 20
def solve(s):
    return ' '.join(map(str.capitalize, s.split(' ')))
