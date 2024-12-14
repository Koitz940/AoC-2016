with open("data") as f:
    line = f.read()

line.replace(" ", "")

def part1(code):
    i = 0
    answer = 0
    while i < len(code):
        match code[i]:
            case "(":
                close = i + code[i:].index(")")
                x = i + code[i:close].index("x")
                amount = int(code[i+1:x])
                times = int(code[x+1:close])
                answer += amount * times
                i = close + amount + 1
            case _:
                i += 1
                answer += 1
    return answer


def part2(code):
    i = 0
    answer = 0
    while i < len(code):
        match code[i]:
            case "(":
                close = i + code[i:].index(")")
                x = i + code[i:close].index("x")
                amount = int(code[i + 1:x])
                times = int(code[x + 1:close])
                answer += times * part2(code[close + 1: close + 1 + amount])
                i = close + amount + 1
            case _:
                i += 1
                answer += 1
    return answer


def solve(code):
    i = 0
    answer1 = 0
    answer2 = 0
    while i < len(code):
        match code[i]:
            case "(":
                close = i + code[i:].index(")")
                x = i + code[i:close].index("x")
                amount = int(code[i + 1:x])
                times = int(code[x + 1:close])
                answer1 += amount * times
                answer2 += times * part2(code[close + 1: close + 1 + amount])
                i = close + amount + 1
            case _:
                i += 1
                answer1 += 1
                answer2 += 1
    return answer1, answer2
print(solve(line))
