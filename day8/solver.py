with open("dataset", "r") as fp:
    data = fp.readlines()


data = [list(map(int, line.strip())) for line in data]


def count_visible_trees(line, first_index, reversed=False, flip=False):
    maximum = -1
    result = []
    line = list(line)
    for count, tree in enumerate(line):
        if tree <= maximum:
            continue
        else:
            maximum = tree
            second_index = count if not reversed else len(line) - 1 - count
            result.append((first_index, second_index) if not flip else (second_index, first_index))
    return result


total = []
for count, line in enumerate(data):
    total += count_visible_trees(line, count)
    total += count_visible_trees(reversed(line), count, reversed=True)

for count, line in enumerate(zip(*data)):
    total += count_visible_trees(line, count, flip=True)
    total += count_visible_trees(reversed(line), count, flip=True, reversed=True)


print(len(set(total)))


# part 2
# ------> (x)
# |
# |
# |
# V
# (y)


reversed_data = list(zip(*data))


def build_tree_mark(x, y, tree_height):
    left_trees = reversed(data[y][:x])
    right_trees = data[y][x + 1 :]

    top_trees = reversed(reversed_data[x][:y])
    bot_trees = reversed_data[x][y + 1 :]

    def get_score(trees):
        score = 0
        for tree in trees:
            score += 1
            if tree >= tree_height:
                break
        return score

    return (
        get_score(left_trees) * get_score(right_trees) * get_score(top_trees) * get_score(bot_trees)
    )


total = []
for y in range(len(data)):
    line = []
    for x in range(len(data[0])):
        line.append(build_tree_mark(x, y, data[y][x]))
    total.append(max(line))

print(max(total))
