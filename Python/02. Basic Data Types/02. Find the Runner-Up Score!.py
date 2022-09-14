# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
# Score = 10
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    a=set(arr)
    a.remove(max(a))
    print(max(a))
