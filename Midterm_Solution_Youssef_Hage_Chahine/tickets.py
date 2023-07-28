# import the txt file :
tickets_list = []
with open('ticket_list.txt', 'r') as file:
    ticket_data = file.readlines()

for tik_data in ticket_data:
    ticket_list = tik_data.strip().split(", ")
    
    if len(ticket_list) == 5:
        tickets_list.append(ticket_list)


#print(tickets_list)

# Admin users
# display staistics


def displayStatistics(tickets_list):
    max_event_id = None
    max_event_count = 1
    event_count = {}

    for tikts in tickets_list:
        event_id = tikts[1]
        event_count[event_id] = event_count.get(event_id, 0) + 1
        if event_count[event_id] > max_event_count:
            max_event_id = event_id
            max_event_count = event_count[event_id]
    
    return max_event_id, max_event_count

max_event_id, max_event_count = displayStatistics(tickets_list)

print(f'Max event id: {max_event_id}, {max_event_count}')