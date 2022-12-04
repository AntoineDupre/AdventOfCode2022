# Load dataset
with open("dataset", "r") as fp:
    data = fp.readlines()

data = list(map(str.strip, data))


def compute_prio(letter):
    return (
        ord(letter) - lower_offset if letter.islower() else ord(letter) - upper_offset
    )


# Part 1

lower_offset = ord("a") - 1
upper_offset = ord("A") - 27
mistakes = [
    set(set(d[: int(len(d) / 2)]) & set(d[int(len(d) / 2) :])).pop() for d in data
]

error = sum((compute_prio(mistake) for mistake in mistakes))
print(error)

# Part 2

def group_iterator():
    data_len = len(data)
    index = 0
    while index < data_len:
        yield data[index], data[index + 1], data[index + 2]
        index += 3


print(sum(compute_prio(set(set(x) &set(y) & set(z)).pop()) for x, y, z in group_iterator()))

