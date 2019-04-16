class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None


pre_list = [1, 2, 4, 7, 3, 5, 6, 8]
in_list = [4, 7, 2, 1, 5, 3, 8, 6]
root_node = None


def construct_tree(root, pre_lst, in_lst):
    if not root:  # 根节点不存在
        root = TreeNode(pre_lst[0])
    left_in_lst = in_lst[0: in_lst.index(pre_lst[0])]
    right_in_lst = [] if in_lst.index(pre_lst[0]) == len(in_lst) - 1 else in_lst[in_lst.index(pre_lst[0])+1:]
    left_pre_lst = pre_lst[1: 1 + len(left_in_lst)]
    right_pre_lst = pre_lst[1 + len(left_in_lst):]
    if len(left_pre_lst) > 0 or len(left_in_lst) > 0:
        root.left_child = construct_tree(root_node, left_pre_lst, left_in_lst)
    if len(right_pre_lst) > 0 or len(right_in_lst) > 0:
        root.right_child = construct_tree(root_node, right_pre_lst, right_in_lst)
    return root


root_node = construct_tree(root_node, pre_list, in_list)
print(root_node.left_child.left_child.right_child.value)