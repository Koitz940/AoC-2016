with open("data") as f:
    lines = f.readlines()

for line in range(len(lines)):
    lines[line] = lines[line].strip()

def part1(stuff):
    for thing in range(len(stuff)):
        stuff[thing] = stuff[thing].replace("-", "")
    def is_real(lne):
        secret = lne[:-10]
        letters = set([i for i in secret])
        counted = [secret.count(i) for i in letters]
        counted.sort()
        counted.reverse()
        numb = int(lne[-10:-7])
        order = lne[-6:-1]
        quantity = [secret.count(i) for i in order]
        if counted[:5] != quantity:
            return 0
        for i in range(1, len(order)):
            if quantity[i] == quantity[i-1] and ord(order[i]) < ord(order[i-1]):
                return 0
        return numb
    return sum(list(map(is_real, stuff)))


def part2(stuff):
    base = ord("a")
    for thing in range(len(stuff)):
        stuff[thing] = stuff[thing].replace("-", "")
    for lin in stuff:
        numb = int(lin[-10:-7])
        secret = lin[:-10]
        new = ""
        for i in range(len(secret)):
            new += chr((numb + ord(secret[i]) - base) % 26 + base)
        print(new)
        if new.startswith("northpole"):
            return numb

print(part2(lines))
