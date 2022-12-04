def part1(data):
    elves = []
    elf = 0

    for calories in data:
        if calories != '':
            elf += int(calories)
        else:
            elves.append(elf)
            elf = 0

    return max(elves)

################################################################################


def part2(data):
    elves = []
    elf = 0

    for calories in data:
        if calories != '':
            elf += int(calories)
        else:
            elves.append(elf)
            elf = 0

    elves.sort(reverse=True)
    ans = elves[0] + elves[1] + elves[2]

    return ans

data = open("input.txt", "r").readlines()
#data = open("example.txt", "r").readlines()

#data = [[int(n) for n in line] for line in data]
#data = [int(n) for n in data]
#data = [line.split(" ") for line in data]
#data = [line.split("-") for line in data]
#data = [line.split(",") for line in data]
#data = [line.split(",") for line in data][0]
data = [line.strip("\n") for line in data]
#data = [line[:-1] for line in data]
#data = [re.sub(r" -> ", r",", line) for line in data]
#data = [re.sub(r" \| ", r" ", line) for line in data]

print(part1(data))
print(part2(data))
