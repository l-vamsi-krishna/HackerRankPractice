# https://www.hackerrank.com/challenges/finding-the-percentage/problem
# Score = 10
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    query_marks=list(student_marks.get(query_name))
    print("%.2f"%(sum(query_marks)/len(query_marks)))
