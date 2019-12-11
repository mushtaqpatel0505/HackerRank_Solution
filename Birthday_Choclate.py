def birthday(s, d, m):
    c=0
    for i in range(len(s)):
        if sum(s[i:m+i]) == d:
            c += 1
    return c

n = int(input().strip())

s = list(map(int, input().rstrip().split()))

dm = input().rstrip().split()

d = int(dm[0])

m = int(dm[1])

result = birthday(s, d, m)
