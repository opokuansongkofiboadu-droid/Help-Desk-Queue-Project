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
        print("Ticket ID has been assigned to a different task. Type in a different ID")
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
        return False
def age_priority_queue(priority_queue):
    new_queue=[]

    if priority_queue:
        for item in priority_queue:
            priority=item[0]
            order=item[1]
            ticket=item[2]

            if priority > 1:
                priority -= 1

            new_queue.append((priority, order, ticket))
    heapq.heapify(new_queue)
    return new_queue


while True:
    
        command=input("Enter your command(create/escalate/process normal/process priority/undo/view/quit): ").strip().lower()
        if command=="quit":
            break

        elif command=="create":
            ticket_id=input("Enter ticket_id(T_ _ _): ")
            issue=input("What is the issue? ")
        
            ticket=create_ticket(ticket_id,issue)
            add_ticket(normal_queue,ticket,ticket_ids)

        elif command=="escalate":
            ticket_id=input("Enter ticket_id(T_ _ _): ")
            try:
                priority=int(input("What is the priority of this ticket? "))
            except ValueError:
                print("Priotiy must be a number")
                continue

    
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
                priority_queue=age_priority_queue(priority_queue)


        elif command=="undo":
            ticket=undo_resolution(resolved_history)

            if ticket:
                normal_queue.append(ticket)

        elif command=="view":
            view=input("Normal/Priority/Resolved? ").strip().lower()
            if view=="normal":
                if normal_queue:
                    print("Normal Queue")
                    for ticket in normal_queue:
                        print(ticket)
                else:
                    print("Queue is empty")  

            elif view=="priority":
                if priority_queue:
                    print("Priority Queue")
                    for ticket in priority_queue:
                        print(ticket)
                else:
                    print("Queue is empty")

            elif view=="resolved":
                if resolved_history:
                    print("Resolved History")
                    for ticket in resolved_history:
                        print(ticket)
                else:
                    print("Resolved history is empty")
            else:
                print("Invalid command")

        else:
            print("Invalid command")

