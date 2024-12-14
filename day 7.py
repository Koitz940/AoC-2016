with open("data") as f:
    lines = f.readlines()

for line in range(len(lines)):
    lines[line] = lines[line].strip()


def part1(stuff):
    def istls(ip):
        listyes = []
        listno = []
        index = 0
        current = "]"
        for i in range(len(ip)):
            match current:
                case "]":
                    if ip[i] == "[":
                        listyes.append(ip[index:i])
                        index = i + 1
                        current = "["
                case "[":
                    if ip[i] == "]":
                        listno.append(ip[index:i])
                        index = i + 1
                        current = "]"
        if index != len(ip) - 1:
            listyes.append(ip[index:])
        def abba(liss):
            for j in liss:
                for a in range(len(j)-3):
                    if j[a] == j[a+3] and j[a+1] == j[a+2] and j[a] != j[a+1]:
                        return True
            return False
        return 1 if abba(listyes) and not abba(listno) else 0
    return sum(list(map(istls, stuff)))


def part2(stuff):
    def ssllist(ip):
        noblist = []
        blist = []
        index = 0
        current = "]"
        for i in range(len(ip)):
            match current:
                case "]":
                    if ip[i] == "[":
                        noblist.append(ip[index:i])
                        index = i + 1
                        current = "["
                case "[":
                    if ip[i] == "]":
                        blist.append(ip[index:i])
                        index = i + 1
                        current = "]"
        if index != len(ip) - 1:
            noblist.append(ip[index:])
        def aba(xyx, yxy):
            pairs = []
            for j in xyx:
                for a in range(len(j)-2):
                    if j[a] == j[a+2] and j[a] != j[a+1]:
                        pairs.append(j[a:a+3])
            opairs = []
            for j in yxy:
                for a in range(len(j)-2):
                    if j[a] == j[a+2] and j[a] != j[a+1]:
                        opairs.append(j[a:a+3])
            for pair in pairs:
                if pair[1] + pair[0] + pair[1] in opairs:
                    return 1
            return 0
        return aba(noblist, blist)
    return sum(list(map(ssllist, stuff)))


print(part2(lines))
