# https://www.hackerrank.com/challenges/nested-list/problem
# Score = 10
if __name__ == '__main__':
    data={}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        data.update({name:score})
    set_scores=set(data.values())
    list_scores=list(set_scores)
    list_scores.sort()
    second_last_score=list_scores[1]
    names_list=[]
    for name,score in data.items():
        if score == second_last_score:
            names_list.append(name)
    names_list.sort()
    for names in names_list:
        print(names)
