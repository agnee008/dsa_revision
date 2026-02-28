class ListNode:
    def __init__(self) -> None:
        pass
    

def sortList(head: ListNode):
    if not head or not head.next:
        return head
    
    # Split in two halves
    left = head
    right = getMid(head)
    temp = right.next
    right.next = None
    right = temp
    
    left = sortList(left)
    right = sortList(right)
    return mergeList(left,right)

def getMid(head):
    slow, fast = head, head.next
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def mergeList(list1, list2):
    tail = dummy =ListNode()
    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
        
    if list1:
        tail.next = list1
    if list2:
        tail.next = list2
    return dummy.next
    