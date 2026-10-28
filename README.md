## Help-Desk Queue Project

# Project purpose
The Help-Desk Queue project is a command-line program that is used to manage support tickets.Normal tickets are handled in FIFO order with the use of deque.Escalated tickets are handled mainly by priortiy followed by order for elemetns with tied priorities by using heapq module. The resolved tikcets are stored in a stack so the most recent resolution can be undone.

# Data structures and why each one was chosen.
Deque-It was used for the normal ticket queue because it supports FIFO
Heapq-It was used for priority queue because it allows tickets to be processed based on priority mainly and then also uses order for priority ties
List-It was used for the resolved history stack.This is because it supports LIFO and would allow us to remove tha last entry from the resolved history is found out that the issue wasn't fully delt with.
Set-It was used for ticket IDs. Suited for checking duplicate IDs

# Manual Test Table
| Test case | Expected result | Actual result |
|---|---|---|
| Create two tickets with the same ID | Second ticket should be rejected | Duplicate-ID message displayed |
| Process an empty normal queue | Program should not crash | `"Queue is empty"` displayed |
| Process an empty priority queue | Program should not crash | `"Priority queue is empty"` displayed |
| Undo when resolved history is empty | Program should not crash | `"Resolved history is empty"` displayed |
| Enter an invalid command | Program should reject it | `"Invalid command"` displayed |
| Escalate two tickets with equal priority | Earlier escalated ticket should be processed first | Tickets processed in expected order |
| Enter non-numeric priority | Program should not crash | Error handled and command loop continued |
| Apply priority ageing | Remaining ticket priorities should improve after processing one | Ageing worked as expected |

# Benchmark Test(List vs Deque)
A benchmark was performed using 10,000 items to compare rremoving elements from the front of a python list using pop(0) with removing elements form a deque using popleft()

The list removed all the elements in approximately 0.0831 seconds whilst deque removed all the elemts using popleft() in approximately 0.000505 seconds.
This substantiates the claim that list.pop(0) is O(n) becuase the remaining elements must shidt, while deque.popleft() is O(1) becuase it is dedigned for efficient removal from the front.These numbers are not universal but the trend will be seen clearly especially when as the number of items increases.


# Complexity Reasoning
The Help-Desk Queue uses different data structures because each one provides efficient operations for a specific task.
- Adding a normal ticket with deque.append() is O(1).
- Processing a normal ticket with deque.popleft() is O(1).
- Checking whether a ticket ID already exists in a set is O(1) on average.
- Finding a particular normal ticket to escalate is O(n) because the program may need to search through the queue.
- Adding an escalated ticket with heapq.heappush() is O(log n).
- Processing a priority ticket with heapq.heappop() is O(log n).
- Adding a resolved ticket with list.append() is O(1).
- Undoing the latest resolution with list.pop() is O(1).

# How the program works
create — create a new normal ticket
escalate — move a normal ticket into the priority queue
process normal — resolve the next normal FIFO ticket
process priority — resolve the highest-priority ticket and then age the remaining priority tickets
undo — restore the most recently resolved ticket to the normal queue
view — inspect the normal queue, priority queue, or resolved history
quit — exit the program