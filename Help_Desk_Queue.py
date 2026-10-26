from collections import deque
import heapq



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
        print("It has been assigned to a different task")
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

def undo_resolution(resolved_history):
    if resolved_history:
        return resolved_history.pop()
        
    else:
        print("Resolved history is empty")
        return False

    

priority_queue=[]
order=0
def remove_ticket_from_normal_queue(normal_queue, ticket_id ):
    for ticket in normal_queue:
        if ticket["id"]==ticket_id:
            normal_queue.remove(ticket)
            return ticket
    else:
        print("Ticket id not found")


def escalate_ticket(priority_queue,priority,order,ticket):
    order+=1
    heapq.heappush(priority_queue,(priority,order,ticket))
    return order

def process_priority_ticket(priority_queue):
    if priority_queue:
       heap_entry= heapq.heappop(priority_queue)
       return heap_entry[2] 
    else:
        print("Priority queue is empty")



while True:
    
        command=input("Enter your command(create/escalate/process normal/process priortiy/undo/view/quit): ").strip().lower()
        if command=="quit":
            break

        elif command=="create":
            ticket_id=input("Enter ticket_id(T___): ")
            issue=input("What is the issue? ")
        
            ticket=create_ticket(ticket_id,issue)
            add_ticket(normal_queue,ticket,ticket_ids)

        elif command=="escalate":
            ticket_id=input("Enter ticket_id(T___): ")
            priority=int(input("What is the priority of this ticket? "))

    
            ticket=remove_ticket_from_normal_queue(normal_queue,ticket_id)
    
            if ticket:
                order = escalate_ticket(priority_queue, priority, order, ticket)

        elif command=="process normal":
            ticket=process_normal_ticket(normal_queue)
            if ticket:
                add_to_resolved_history(resolved_history, ticket)

        
        elif command=="process priority":
            ticket=process_priority_ticket(priority_queue)

            if ticket:
                add_to_resolved_history(resolved_history,ticket)

        elif command=="undo":
            ticket=undo_resolution(resolved_history)

            if ticket:
                normal_queue.append(ticket)

        elif command=="view":
            view=input("Normal/Prioity/Resolved? ").strip().lower()
            if view=="normal":
                print("Normal Queue")
                for ticket in normal_queue:
                    print(ticket)
            elif view=="priority":
                print("Priority Queue")
                for ticket in priority_queue:
                    print(ticket)
            elif view=="resolved":
                print("Resolved History")
                for ticket in resolved_history:
                    print(ticket)
            else:
                print("Invalid command")

        else:
            print("Invalid command")
