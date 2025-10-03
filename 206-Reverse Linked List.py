class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        currnode , prevnode = head , None 
        while currnode:
            nextnode = currnode.next
            currnode.next = prevnode
            prevnode = currnode
            currnode =nextnode
        return prevnode