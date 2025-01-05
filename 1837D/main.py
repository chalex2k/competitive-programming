from fastio import *

# раскраска скобочных последовательностей

def solve(n: int, s: str):
    if n % 2 == 1:
        print(-1)
        return

    ans = [1]
    is2colors = False
    curr_color = 1
    is_positive_balance = s[0] == '('
    balance = 1 if s[0] == '(' else -1
    for c in s[1:]:
        balance += 1 if c == '(' else -1
        if is_positive_balance:
            if balance >= 0:
                ans.append(curr_color)
            else:
                is_positive_balance = False
                curr_color = 3 - curr_color
                ans.append(curr_color)
                is2colors = True
        else:
            if balance <= 0:
                ans.append(curr_color)
            else:
                is_positive_balance = True
                curr_color = 3 - curr_color
                ans.append(curr_color)
                is2colors = True

    if balance != 0:
        print(-1)
        return

    print(2 if is2colors else 1)
    print(*ans)


def main():
    for _ in range(ii()):
        n = ii()
        s = si()
        solve(n, s)


if __name__ == '__main__':
    main()
