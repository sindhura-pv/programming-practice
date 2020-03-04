# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lis):

        if not lis:
            return None

        if len(lis) == 1:
            return lis[0]

        lists = []
        for node in lis:
            if node:
                lists.append(node)

        head = temp = ListNode(float('inf'))

        while lists:

            temp_val = float('inf')

            for i, node in enumerate(lists):
                if node.val < temp_val:
                    temp_val = node.val
                    index = i

            temp.next = ListNode(temp_val)
            temp = temp.next

            if lists[index].next:
                lists[index] = lists[index].next

            else:
                del lists[index]

        return head.next
