with open("dataset", "r") as fp:
    data = fp.readlines()

data = [d.strip() for d in data]


def line_extractor(data):
    def create_range(entries):
        return set(range(int(entries[0]), int(entries[1]) + 1))

    for line in data:
        yield (create_range(elf.split("-")) for elf in line.split(","))


def part1(data):
    count = 0
    for a, b in line_extractor(data):
        if a & b == b or a & b == a:
            count += 1
    return count


def part2(data):
    count = 0
    for a, b in line_extractor(data):
        intersection = a & b
        if intersection:
            count += 1
    return count


result_part_1 = part1(data)
result_part_2 = part2(data)


print(result_part_1, result_part_2)
