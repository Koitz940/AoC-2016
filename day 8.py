with open("data") as f:
    lines = f.readlines()

for line in range(len(lines)):
    lines[line] = lines[line].strip()


def solve(orders, width, height):
    grid = [[0 for _ in range(width)] for _ in range(height)]
    def do_order(order, panel):
        order = order.split()
        match order[0]:
            case "rect":
                index = order[1].find("x")
                for i in range(int(order[1][:index])):
                    for j in range(int(order[1][index + 1:])):
                        panel[j][i] = 1
            case "rotate":
                match order[1]:
                    case "row":
                        index = int(order[2][2:])
                        amount = int(order[-1])
                        on = [i for i in range(width) if panel[index][i] == 1]
                        panel[index] = [0 for _ in range(width)]
                        for pixel in on:
                            panel[index][(pixel + amount) % width] = 1
                    case "column":
                        index = int(order[2][2:])
                        amount = int(order[-1])
                        on = [i for i in range(height) if panel[i][index] == 1]
                        for i in range(height):
                            panel[i][index] = 0
                        for pixel in on:
                            panel[(pixel + amount) % height][index] = 1
        return panel
    for exe in orders:
        grid = do_order(exe, grid)
    for row in grid:
        message = ""
        for z in range(width):
            if row[z] == 1:
                message += "# "
            else:
                message += ". "
        print(message)
    return sum([grid[i][j] for i in range(height) for j in range(width)])


print(solve(lines, 50, 6))
