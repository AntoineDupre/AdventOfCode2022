with open("dataset", "r") as fp:
    data = fp.readlines()

data = [d[:-1] for d in data][0]


def find_unique(group_size):
    for index in range(0, len(data) - group_size):
        group = set(data[index : index + group_size])
        if len(group) == group_size:  # All different:
            return index + group_size


def part1():
    print(find_unique(4))


def part2():
    print(find_unique(14))


part1()
part2()
