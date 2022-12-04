# Load dataset
with open("dataset", "r") as fp:
    data = fp.readlines()


# Part 1

lower_offset = ord("a") - 1
upper_offset = ord("A") - 27
mistakes = [
    set(set(d[: int(len(d) / 2)]) & set(d[int(len(d) / 2) :])).pop() for d in data
]

error = sum(
    [
        ord(mistake) - lower_offset
        if mistake.islower()
        else ord(mistake) - upper_offset
        for mistake in mistakes
    ]
)

# Part 2
