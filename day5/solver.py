with open("dataset", "r") as fp:
    data = fp.readlines()

data = [d[:-1] for d in data]


def parse_stack_schema(data):
    last_schema_index = None
    schema_line_start = None
    for line_counter, line in enumerate(data):
        if line[1] == "1":
            schema_line_start = line_counter
            last_schema_index = len(line)
            break

    def build_stack(index):
        stack = []
        for line in range(schema_line_start - 1, -1, -1):
            try:
                char = data[line][index]
                if char == " ":
                    break
                else:
                    stack.append(char)
            except IndexError:
                break

        return stack

    stacks = [build_stack(index) for index in range(1, last_schema_index, 4)]
    return stacks, line_counter


def parse_motion(data, ignore_lines):
    return [
        tuple(
            map(
                int,
                d.replace("move ", "").replace("from ", "").replace("to ", "").strip().split(" "),
            )
        )
        for d in data[ignore_lines + 1 :]
    ]


def proceed(move_crain):
    stacks, schema_line = parse_stack_schema(data)
    motions = parse_motion(data, schema_line + 1)
    for repeat, start, end in motions:
        move_crain(stacks, start - 1, end - 1, repeat)

    print("".join([stack[-1] for stack in stacks if stack]))


def part1():
    def move_crain(stacks, start, end, repeat):
        for _ in range(repeat):
            try:
                stacks[end].append(stacks[start].pop())
            except IndexError:
                pass

    proceed(move_crain)


def part2():
    def move_crain(stacks, start, end, repeat):
        stacks[end] += reversed([stacks[start].pop() for _ in range(repeat)])

    proceed(move_crain)


part1()
part2()
