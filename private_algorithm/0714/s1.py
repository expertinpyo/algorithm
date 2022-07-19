a = list(range(1, 10))
slow = fast = head

while fast and fast.next:
    fast = fast.next.next
    print(fast)