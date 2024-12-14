with open("data") as f:
    line = f.read()

def part1(data):
    guide = data.split()
    direction = 1j
    position = 0
    for i in guide:
        direction *= 1j if i[0] == "L" else -1j
        position += direction * int(i[1:-1])
    return int(abs(position.imag) + abs(position.real))


def part2(data):
    guide = data.split()
    direction = 1j
    position = 0+0j
    cache = set()
    check = False
    for i in guide:
        if check:
            break
        direction *= 1j if i[0] == "L" else -1j
        for _ in range(int(i[1:-1])):
            position += direction
            if position in cache:
                check = not check
                break
            cache.add(position)
    return int(abs(position.imag) + abs(position.real))
