# https://www.hackerrank.com/challenges/python-lists/problem
# Score = 10
if __name__ == '__main__':
    N = int(input())
    arr=[]
    for i in range(N):
        user_command=input()
        command_value=user_command.split()[0]
        if command_value=='insert':
            arr.insert(int(user_command.split()[1]),int(user_command.split()[2]))
        elif command_value=='print':
            print(arr)
        elif command_value=='remove':
            print(arr)
            arr.remove(int(user_command.split()[1]))
        elif command_value=='append':
            arr.append(int(user_command.split()[1]))
        elif command_value=='sort':
            arr.sort()
        elif command_value=='pop':
            arr.pop()
        elif command_value=='reverse':
            arr.reverse()
