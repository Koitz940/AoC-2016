with open("data") as f:
    lines = f.readlines()

for line in range(len(lines)):
    lines[line] = lines[line].strip()

def part1(stuff):
    columns = ([stuff[i][j] for i in range(len(stuff))] for j in range(len(stuff[0])))
    answer = ""
    for i in columns:
        letters = list(set([j for j in i]))
        counter = [i.count(letters[j]) for j in range(len(letters))]
        answer += letters[counter.index(max(counter))]
    return answer


def part2(stuff):
    columns = ([stuff[i][j] for i in range(len(stuff))] for j in range(len(stuff[0])))
    answer = ""
    for i in columns:
        letters = list(set([j for j in i]))
        counter = [i.count(letters[j]) for j in range(len(letters))]
        answer += letters[counter.index(min(counter))]
    return answer


print(part2(lines))
