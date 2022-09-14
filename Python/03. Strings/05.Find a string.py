# https://www.hackerrank.com/challenges/find-a-string/problem
# Score = 10

def count_substring(string, sub_string):
    found=0
    count=0
    while found>-1:
        found=string.find(sub_string,found)+1
        if found == 0:
            break
        count+=1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
