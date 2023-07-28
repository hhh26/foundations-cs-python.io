import datetime



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

## display staistics


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


## Book a ticket:
## 1st step admin input:
username = input('enter a name: ')
event_id = input('enetr the event id: ')
priority = input('enter priority lvl from 0 to 3: ')


### 2nd step get the curret date  
def get_date():
    return datetime.datetime.now().strftime('%Y%m%d') #https://www.programiz.com/python-programming/datetime/strftime# 
# return the current time in this format yyyymmdd

### 3rd step create next ticket id:
def new_ticket():
    with open('ticket_list.txt', 'r') as file:
        last_ticket = file.readlines()[-1] # the last tikcket in the list 
        last_ticket_id = int(last_ticket.split(', ')[0].lstrip('tick'))
        return f"tick{last_ticket_id + 1:02}"

current_date = get_date()
new_ticket_id = new_ticket()

new_ticket_list = f"{new_ticket_id}, {event_id}, {username}, {current_date}, {priority}\n"

with open('ticket_list.txt', 'a') as file:
    file.write(new_ticket_list)
print('ticket list updated')


