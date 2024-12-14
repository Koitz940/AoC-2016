with open("data") as f:
    lines = f.readlines()

for i in range(len(lines)):
    lines[i] = lines[i][:-1]
letters = {
    "D": -1j,
    "U": 1j,
    "R": 1,
    "L": -1
}
panel1 = {
    0 + 2j: 1,
    1 + 2j: 2,
    2 + 2j: 3,
    0 + 1j: 4,
    1 + 1j: 5,
    2 + 1j: 6,
    0 + 0j: 7,
    1 + 0j: 8,
    2 + 0j: 9
}

panel2 = {
    0 + 2j: "1",
    -1 + 1j: "2",
    0 + 1j: "3",
    1 + 1j: "4",
    -2 + 0j: "5",
    -1 + 0j: "6",
    0 + 0j: "7",
    1 + 0j: "8",
    2 + 0j: "9",
    -1 - 1j: "A",
    0 - 1j: "B",
    1 - 1j: "C",
    0 - 2j: "D"
}


def ending(cur: complex, line: str, panel: dict) -> complex:
    for j in line:
        holder = cur
        cur += letters[j]
        if cur not in panel:
            cur = holder
    return cur


def part1(stuff):
    code = 0
    current = 1 + 1j
    for z in range(len(stuff)):
        current = ending(current, stuff[z], panel1)
        print(panel1[current])
        code += panel1[current] * 10**(len(stuff)-z-1)
    return code


def part2(stuff):
    code = ""
    current = 1 + 1j
    for z in range(len(stuff)):
        current = ending(current, stuff[z], panel2)
        print(panel2[current])
        code += panel2[current]
    return code


print(part2(lines))