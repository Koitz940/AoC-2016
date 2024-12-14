with open("data") as f:
    lines = f.readlines()

for line in range(len(lines)):
    lines[line] = lines[line].split()


def part1(stuff):
    return sum(list(
        map(lambda x: 1 if x[0] + x[1] > x[2] and x[0] + x[2] > x[1] and x[2] + x[1] > x[0] else 0,
            [list(map(int, i)) for i in stuff])))


def part2(stuff):
    new_list = []
    for column in range(3):
        for i in range(len(stuff)//3):
            new_list.append([stuff[j][column] for j in range(3*i, 3*i + 3)])
    return sum(list(
        map(lambda x: 1 if x[0] + x[1] > x[2] and x[0] + x[2] > x[1] and x[2] + x[1] > x[0] else 0,
            [list(map(int, i)) for i in new_list])))
