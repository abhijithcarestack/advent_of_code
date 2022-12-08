file = open("inputs.txt", "r")
values = file.read()
inputvalues = values.splitlines()


def printTree(root, level=0):
    print("--" * level+root.name, root.size)
    for child in root.children:
        printTree(child, level + 1)


class Node:
    def __init__(self, name, size) -> None:
        self.name = name
        self.size = size
        self.children = []
        self.parent = None


file = Node('/', 0)
current = file
for i in inputvalues:
    if i[0] == '$':
        input = i.split(' ')
        if input[1] == 'cd':
            if input[2] == '/':
                current = file
            elif input[2] == '..':
                current = current.parent
            else:
                newNode = Node(input[2], 0)
                newNode.parent = current
                current.children.append(newNode)
                current = newNode

    else:
        input = i.split(' ')
        if input[0] != 'dir':
            newNode = Node(input[1], int(input[0]))
            newNode.parent = current
            current.children.append(newNode)

sizes = set()


tot = 0


def post_order(root: Node):
    if not root.children:
        return root.size

    total = 0
    for child in root.children:

        total += post_order(child)

    # if (root.children != []):
    sizes.add(total)
    if total < 100000:
        global tot
        tot += total
    return total


printTree(file)
post_order(file)
# print(tot)
