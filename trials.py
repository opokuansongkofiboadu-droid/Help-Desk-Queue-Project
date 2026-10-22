def push(stack,item):
    """Adds a new entry to the stack"""
    stack.append(item)
    return stack

def pop_stack(stack):
    """removes the latest entry from the stack"""
    if stack:
        return stack.pop()
    else:
        print("List is empty")

def peek(stack):
    """Views the next item to be processed"""
    if stack:
        last=stack[-1]
        return last
    else :
        print("List is empty")

def add_queue(queue,item):
    """Adds an entry to the queue"""
    queue.append(item)

def remove_queue(queue):
    """Removes first entry"""
    if queue:
        return queue.pop(0)
    else:
        print("Queue is empty")

def view_queue(queue):
    "View the entry up for processing"
    if queue:
        first=queue[0]
        return first
    else:
        print("Queue is empty")

from collections import deque
queue=deque()

def add_queue(queue,item):
    """Adds a new entry to the queue"""
    queue.append(item)

def remove_item(queue):
    """Removes first entry"""
    if queue:
        return queue.popleft()
    else:
        print("Queue is empty.")

def view_item(queue):
    """Checks next entry to be processed"""
    if queue:
        first=queue[0]
        return first
    else:
        print("Queue is empty.")

import heapq
tickets=[]

def add_to_heap(tickets,item):
        heapq.heappush(tickets,item)

def remove_from_heap(tickets):
    if tickets:
        return heapq.heappop(tickets)
    else:
        print("Collection is empty")

def view_heap(tickets):
    if tickets:
        primary= tickets[0]
        return primary
    else:
        print("Collection is empty")

ticket1 = (2, 1, "Printer issue")
ticket2 = (1, 2, "Server down")
ticket3 = (1, 3, "Network outage")

#add_to_heap(tickets,ticket1)
#add_to_heap(tickets,ticket2)
#add_to_heap(tickets,ticket3)

print(remove_from_heap(tickets))
print(remove_from_heap(tickets))
print(remove_from_heap(tickets))
