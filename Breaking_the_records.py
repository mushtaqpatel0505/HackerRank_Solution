
def breakingRecords(scores):
    c_break = 0
    c_worst=0
    max_score = scores[0]
    low_score = scores[0]
    for x in scores:
        if x > max_score:
            c_break+= 1
            max_score = x
        elif x < low_score:
            c_worst += 1
            low_score = x
    return c_break, c_worst

n = int(input())

scores = list(map(int, input().rstrip().split()))

result = breakingRecords(scores)
