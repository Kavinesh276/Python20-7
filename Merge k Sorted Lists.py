from heapq import heappush, heappop

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    min_heap = []
    for l in lists:
        while l:
            heappush(min_heap, l.val)
            l = l.next
    dummy = ListNode()
    current = dummy
    while min_heap:
        current.next = ListNode(heappop(min_heap))
        current = current.next
    return dummy.next
