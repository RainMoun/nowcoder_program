class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None


def find_path(node, path_lst, sum_value):
    path_lst.append(node.value)
    if not node.left_child and not node.right_child:
        if sum(path_lst) == sum_value:
            print(path_lst)
    if node.left_child:
        find_path(node.left_child, path_lst, sum_value)
    if node.right_child:
        find_path(node.right_child, path_lst, sum_value)
    path_lst.pop(-1)


if __name__ == '__main__':
    node_10 = TreeNode(10)
    node_5 = TreeNode(5)
    node_4 = TreeNode(4)
    node_7 = TreeNode(7)
    node_12 = TreeNode(12)
    node_10.left_child = node_5
    node_10.right_child = node_12
    node_5.left_child = node_4
    node_5.right_child = node_7
    find_path(node_10, [], 22)

