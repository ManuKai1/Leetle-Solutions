def solve(head):
    if head == None:
      return None
    n = 0
    l = []
    while head:
        l.append(head)
        head = head.next
        n += 1
    i = 0
    while i < n//2:
        l[i].next = l[n - i - 1]
        l[n - i - 1].next = l[i+1]
        i += 1
    l[i].next = None    
    return l[0]
