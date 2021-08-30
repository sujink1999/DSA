# Given the head of a singly linked list, reverse the list, and return the reversed list.
# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        if not head or not head.next:
            return head
        curr = head
        next = head.next
        
        while next:
            curr.next = prev
            prev = curr
            temp = next.next
            next.next = curr
            curr = next
            next = temp
            
        return curr