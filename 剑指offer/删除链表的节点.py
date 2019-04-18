class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


def delete_node(head_node, delete_node):
    if not head_node or not delete_node:
        return
    if delete_node.next:
        p_next = delete_node.next
        delete_node.value = p_next.value
        delete_node.next = p_next.next
    elif head_node == delete_node:
        pass
    else:
        p_node = head_node
        while p_node.next != delete_node:
            p_node = p_node.next


p1 = ListNode(1)
p2 = ListNode(2)
p3 = ListNode(3)
p4 = ListNode(4)
p1.next = p2
p2.next = p3
p3.next = p4
delete_node(p1, p4)
p_node = p1
while p_node:
    print(p_node.value)
    p_node = p_node.next
