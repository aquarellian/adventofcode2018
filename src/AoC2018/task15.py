
def read_subtree(strs):
    children = int(strs[0])
    meta = int(strs[1])
    node = {'children': []}
    length=2
    for i in range(0, children):
        llength, leaf = read_subtree(strs[length:len(strs) - meta])
        node['children'].append(leaf)
        length += llength
    node['metadata'] = strs[length: length + meta]
    length += meta
    return length, node


def sumup_meta(root):
    meta_sum = sum([int(i) for i in root['metadata']])
    for leaf in root['children']:
        meta_sum += sumup_meta(leaf)
    return meta_sum

with open("../resources/task15.txt") as f:
    content = f.readlines()
    tree = {}

    for line in content:
        strs = line.split(' ')
        length, tree = read_subtree(strs)

    print(sumup_meta(tree))
