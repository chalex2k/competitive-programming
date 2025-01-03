import sys

input = lambda: sys.stdin.readline().strip()

YES = 'YES'
NO = 'NO'


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)) + end)


def si():  # string input
    return input()


def ii():  # int input
    return int(input())


def lsi():  # list string input
    return input().split()


def lii():  # list int input
    return list(map(int, input().split()))

# end fast input output
