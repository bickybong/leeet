# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr1 = list1
        curr2 = list2
        new = ListNode()
        head = new
        while curr1 and curr2:
            if curr1.val < curr2.val:
                new.next = curr1
                curr1 = curr1.next
            else:
                new.next = curr2
                curr2 = curr2.next
            new = new.next
        if curr1:
            new.next = curr1
        if curr2:
            new.next = curr2
        return head.next

# time O(m + n)
# space O(1), output doesnt count 