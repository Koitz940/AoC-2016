import hashlib
import itertools
import time

def get_md5(in_string):
    return hashlib.md5(in_string.encode()).hexdigest()

with open("data") as f:
    line = f.read()

def part1(thing):
    answer = ""
    for i in itertools.count(1,1):
        hass = get_md5(thing + str(i))
        if hass[0:5] == "00000":
            answer += hass[5]
            if len(answer) == 8:
                return answer


def part2(thing):
    answer = ""
    letters = []
    indexes = []
    for i in itertools.count(1,1):
        hass = get_md5(thing + str(i))
        if hass[0:5] == "00000" and hass[5].isnumeric():
            if 0 <= int(hass[5]) <= 7 and int(hass[5]) not in indexes:
                indexes.append(int(hass[5]))
                letters.append(hass[6])
                if len(letters) == 8:
                    break
    for i in range(8):
        answer += letters[indexes.index(i)]
    return answer


print(part2(line))
