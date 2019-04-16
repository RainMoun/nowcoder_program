class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None


def find_next_node(node):
    if not node:
        return -1
    if node.right_child:  # 该节点存在右子树
        next_node = node.right_child
        while next_node.left_child:
            next_node = next_node.left_child
        return next_node.value
    else:
        if node.parent.left_child == node:  # 该节点是其父结点的左孩子
            return node.parent.value
        else:
            node = node.parent
            while node.parent and node.parent.right_child == node:
                node = node.parent
            return -1 if not node.parent else node.parent.value


if __name__ == '__main__':
    node_a = TreeNode(1)
    node_b = TreeNode(2)
    node_c = TreeNode(3)
    node_d = TreeNode(4)
    node_e = TreeNode(5)
    node_f = TreeNode(6)
    node_g = TreeNode(7)
    node_h = TreeNode(8)
    node_i = TreeNode(9)
    node_a.left_child = node_b
    node_a.right_child = node_c
    node_b.parent = node_a
    node_c.parent = node_a
    node_b.left_child = node_d
    node_b.right_child = node_e
    node_d.parent = node_b
    node_e.parent = node_b
    node_c.left_child = node_f
    node_c.right_child = node_g
    node_f.parent = node_c
    node_g.parent = node_c
    node_e.left_child = node_h
    node_e.right_child = node_i
    node_h.parent = node_e
    node_i.parent = node_e
    print(find_next_node(node_e))