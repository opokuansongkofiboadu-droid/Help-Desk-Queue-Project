from collections import deque


def create_ticket(ticket_id,issue):
    return {"id":ticket_id,
            "issue":issue}

normal_queue=deque()
def add_ticket(normal_queue,ticket,ticket_ids):
    if unique_ticket_IDs(ticket,ticket_ids):
        normal_queue.append(ticket)

ticket_ids = set()
def unique_ticket_IDs(ticket,ticket_ids):
    if ticket["id"] in ticket_ids:
        print("Id has been assigned to a different task")
        return False
    else:
        ticket_ids.add(ticket["id"])
        return True

def process_normal_ticket(normal_queue):
    if normal_queue:
        return normal_queue.popleft()
    else:
        print("Queue is empty")
        return False

resolved_history =[]
def add_to_resolved_history(resolved_history, ticket):
    resolved_history.append(ticket)

def undo_resolution(resolved_history,normal_queue):
    if resolved_history:
        ticket= resolved_history.pop()
        normal_queue.append(ticket)
    else:
        print("Resolved history is empty")
        return False


ticket1 = {"id": "T001", "issue": "Printer not working"}
ticket2 = {"id": "T002", "issue": "Internet down"}


add_ticket(normal_queue, ticket1, ticket_ids)
add_ticket(normal_queue, ticket2, ticket_ids)

ticket = process_normal_ticket(normal_queue)

if ticket:
    add_to_resolved_history(resolved_history, ticket)
print(resolved_history)