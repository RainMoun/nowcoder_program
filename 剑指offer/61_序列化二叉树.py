# -*- coding:utf-8 -*-
import math
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Serialize(self, root):
        # write code here
        if not root:
            return '#'
        result = str(root.val)
        lst = [root]
        lst_temp = []
        while lst:
            while lst:
                now_node = lst[0]
                lst = lst[1:]
                if now_node:
                    lst_temp.append(now_node.left)
                    lst_temp.append(now_node.right)
                else:
                    lst_temp.append(None)
                    lst_temp.append(None)
            all_none = 1
            temp_str = ''
            for i in lst_temp:
                if i:
                    all_none = 0
                    temp_str += ',' + str(i.val)
                else:
                    temp_str += ',#'
            if all_none == 1:
                break
            result += temp_str
            lst = lst_temp[:]
            lst_temp = []
        return result

    def Deserialize(self, s):
        # write code here
        if s == '#':
            return None
        val_lst = list(s.split(','))
        layer_num = int(math.log(len(val_lst) + 1, 2))
        p_node = TreeNode(int(val_lst[0]))
        if len(val_lst) == 1:
            return p_node
        pre_layer_node = [p_node]
        total_node_num = 1
        for i in range(1, layer_num):
            layer_num = 2 ** i
            layer_node = []
            for j in range(layer_num // 2):
                if not pre_layer_node[j]:
                    total_node_num += 2
                    layer_node.append(None)
                    layer_node.append(None)
                else:
                    if val_lst[total_node_num] != '#':
                        node_left = TreeNode(int(val_lst[total_node_num]))
                        layer_node.append(node_left)
                        total_node_num += 1
                        pre_layer_node[j].left = node_left
                    else:
                        total_node_num += 1
                        layer_node.append(None)
                    if val_lst[total_node_num] != '#':
                        node_right = TreeNode(int(val_lst[total_node_num]))
                        layer_node.append(node_right)
                        total_node_num += 1
                        pre_layer_node[j].right = node_right
                    else:
                        total_node_num += 1
                        layer_node.append(None)
            pre_layer_node = layer_node[:]
        return p_node




p1 = TreeNode(8)
p2 = TreeNode(6)
p3 = TreeNode(10)
p4 = TreeNode(5)
p5 = TreeNode(7)
p6 = TreeNode(9)
p7 = TreeNode(11)
p1.left = p2
p1.right = p3
p2.left = p4
p2.right = p5
p3.left = p6
p4.left = p7
s = Solution()
print(s.Serialize(p1))
print(s.Serialize(s.Deserialize(s.Serialize(p1))))