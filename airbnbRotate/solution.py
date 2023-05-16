def rotate_linked_list(node, shift_by=1): 
    
    # mark the node which has to become the head
    marker = node 
    while shift_by and marker: 
        marker = marker.next
        if not marker: 
            marker = node 
        shift_by -= 1
    
    # move to the end of the list
    tail = marker
    while tail and tail.next: 
        tail = tail.next
    
    while node != marker:
        # grab the first node and attach it to the tail
        tail.next = node
        # move the node to the next node in the list
        node = node.next
        # update tail to the new element
        tail = tail.next
        tail.next = None 
    
    return node
