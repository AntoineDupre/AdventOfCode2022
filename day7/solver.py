from calendar import c


with open("dataset", "r") as fp:
    data = fp.readlines()


class Node:
    def __init__(self, index, name, parent=None):
        self.index = index
        self.name = name
        self.parent = parent
        self.subdirs = {}
        self.files = {}

    @property
    def size(self):
        return sum(self.files.values())

    @property
    def total_size(self):
        total = 0
        for node in self.subdirs.values():
            total += node.total_size
        total += self.size
        return total

    def append_file(self, file, size):
        self.files[file] = int(size)

    def append_directory(self, dir):
        self.subdirs[dir] = Node(self.index + 1, dir, parent=self)


def populate_node_from_ls(node, lines):
    for line in lines:
        if line.startswith("dir"):
            node.append_directory(line.strip().split("dir ")[-1])
        else:
            size, name = line.split(" ")
            node.append_file(name, size)


def command_iterator(data):
    cursor = 0
    while cursor < len(data):
        line = data[cursor]
        assert line.startswith("$")
        index = 1
        while cursor + index != len(data) - 1 and not data[cursor + index].startswith("$"):
            index += 1
        yield data[cursor : index + cursor]
        cursor += index
        if cursor + index == len(data):
            return


def proceed_ls(node, lines):
    populate_node_from_ls(node, lines)


def build_fs():
    root = Node(0, "/", parent=None)
    current_node = root
    for command, *outputs in command_iterator(data):
        if command.startswith("$ ls"):
            proceed_ls(current_node, outputs)
        if command.startswith("$ cd"):
            name = command.split(" ")[-1].strip()
            if name == "..":
                current_node = current_node.parent
            elif name == "/":
                current_node = root
            else:
                current_node = current_node.subdirs[name]
    return root


root_node = build_fs()


def part1(root_node):
    limit = 100000

    def find_file_under_limit(node):
        if node.total_size >= limit:
            total = 0
            for node in node.subdirs.values():
                total += find_file_under_limit(node)
            return total
        else:
            return node.total_size

    return find_file_under_limit(root_node)


expected = 1428881
answer = part1(root_node)
print(answer)
print(answer - expected)
