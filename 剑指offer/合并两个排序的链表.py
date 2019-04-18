class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


def merge(p1, p2):
    if not p1:
        return p2
    if not p2:
        return p1
    if p1.value < p2.value:
        p_merge_node = p1
        p1.next = merge(p1.next, p2)
    else:
        p_merge_node = p2
        p2.next = merge(p1, p2.next)
    return p_merge_node


p1_1 = ListNode(1)
p2_1 = ListNode(3)
p3_1 = ListNode(5)
p4_1 = ListNode(6)
p1_1.next = p2_1
p2_1.next = p3_1
p3_1.next = p4_1
p1_2 = ListNode(2)
p2_2 = ListNode(4)
p3_2 = ListNode(11)
p4_2 = ListNode(12)
p1_2.next = p2_2
p2_2.next = p3_2
p3_2.next = p4_2
node = merge(p1_1, p1_2)
while node:
    print(node.value)
    node = node.next
