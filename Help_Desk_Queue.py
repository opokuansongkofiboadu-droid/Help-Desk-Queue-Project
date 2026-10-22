from collections import deque


def create_ticket(ticket_id,issue):
    return {"id":ticket_id,
            "issue":issue}

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

