import datetime

#----------#
####Admin###
#----------#


# create the special queue sorted by event id and theire event dates:
def specialQueue():
    event_dates = {
        'ev001': '20230802',
        'ev002': '20230803',
        'ev003': '20230804'
    }
    
    special_queue = []


    for event_id in event_dates: 
        special_queue.append((event_id, event_dates[event_id]))
    
    return special_queue
special_queue = specialQueue()


# display evnets dates in the queue sorted by priority



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

#max_event_id, max_event_count = displayStatistics(tickets_list)
#print(f'Max event id: {max_event_id}, {max_event_count}')


## Book a ticket:
## 1st step admin input:

#username = input('enter a name: ')
#event_id = input('enetr the event id: ')
#priority = input('enter priority lvl from 0 to 3: ')


### 2nd step get the curret date  
def get_date():
    return datetime.datetime.now().strftime('%Y%m%d') #https://www.programiz.com/python-programming/datetime/strftime# 
# return the current time in this format yyyymmdd

### 3rd step create next ticket id:
def new_ticket():
    with open('ticket_list.txt', 'r') as file:
        last_ticket = file.readlines()[-1] # the last tikcket in the list 
        last_ticket_id = int(last_ticket.split(', ')[0].lstrip('tick'))
        current_date = get_date()
        return f"tick{last_ticket_id + 1:03}"

#current_date = get_date()
#new_ticket_id = new_ticket()

#new_ticket_list = f"{new_ticket_id}, {event_id}, {username}, {current_date}, {priority}\n"#

#with open('ticket_list.txt', 'a') as file:
#    file.write(new_ticket_list)

#tickets_list.append(new_ticket_list.strip().split(", "))
#print('ticket list updated')


### Display all tickets: (sorting by date and event id)

def sort_tickets(tickets_list):
    for i in range(len(tickets_list)):
        for j in range(i + 1, len(tickets_list)):
            if len(tickets_list[i]) >= 4 and len(tickets_list[j]) >=4:
                if int(tickets_list[i][3]) > int(tickets_list[j][3]) or (int(tickets_list[i][3]) == int(tickets_list[j][3]) and tickets_list[i][1] > tickets_list[j][1]):
                    tickets_list[i], tickets_list[j] = tickets_list[j], tickets_list[i]
            else:
                print('error')
    return tickets_list

#sorted_tickets = sort_tickets(ticket_list)

#print("today s tickets:")
#for ticket in sorted_tickets:
#    if ticket[3] == current_date:
#        print(", ".join(ticket))



### Change Ticket’s Priority:

def change_priority(tickets_list, ticket_to_change, new_priority):
    for ticket in tickets_list:
        if ticket[0] == ticket_to_change:
            ticket[4] = new_priority
            break

#ticket_to_change = input("enter the ticket id: ")
#new_priority = input("enter priority lvl from 0 to 3: ")
#change_priority(tickets_list, ticket_to_change, new_priority)

#for ticket in tickets_list:
#    print(", ".join(ticket))



### Remove tickets: once a ticket is removed, from anywhere in the list but not from the end, i dindt auto-decreced the ticket ID because each ticket ID is UNIQUE 

def remove_tickets(tickets_list, tick_to_remove):
    for ticket in tickets_list:
        if ticket[0] == tick_to_remove:
            tickets_list.remove(ticket)
            print("ticket removed")
            break
        else:
            print("wrong ticket ID")

#tick_to_remove = input('enter the ticket id to remove: ')
#remove_tickets(tickets_list, tick_to_remove)


def todayEvents(tickets_list):
    # https://www.simplilearn.com/tutorials/python-tutorial/global-variable-in-python
    global special_queue, current_date
    #current_date = datetime.datetime.now().strftime('%Y%m%d')
    
    # checking if the current date with any dates in the special queue:
    matching_dates = []
    for event_id, event_date in special_queue:
        if event_date == current_date:
            matching_dates.append(event_date)
    
    if matching_dates:
        # case 1 if the current date == the date in the special queue, we dispalay the tickets and remove them from the queue
        for event_id, event_date in special_queue:
            if event_date == current_date:
                today_events = [ticket for ticket in tickets_list if ticket[1] == event_id]
                sorted_today_events = sorted(today_events, key=lambda ticket : (int(ticket[4]), ticket[1]))

                if sorted_today_events:
                    print('today s ticket:')
                    for ticket in sorted_today_events:
                        print(", ".join(ticket))

                    # removing the ticets from the queue:
                    special_queue = [(ev_id, ev_date) for ev_id, ev_date in special_queue if ev_date != current_date]
                    print('tickets are removed from the queue')
                else:
                    print("no tickets are found for today s event")
                break
            
    # case 2 : if the cuurent date != from the date in the speial queue, ask the admin to input a date and check if
    # there are the same. 

    else:
        input_date = input("enter a date (yyyymmdd): ")
        
        matching_dates = []
        for event_id, event_date in special_queue:
            if event_date == input_date:
                matching_dates.append(event_date)
        
        if matching_dates:
            for event_id, event_date in special_queue:
                if event_date == input_date:
                    today_events = [ticket for ticket in tickets_list if ticket[1] == event_id]
                    sorted_today_events = sorted(today_events, key=lambda ticket: (int(ticket[4]), ticket[1]))

                    if sorted_today_events:
                        print('today s ticket:')
                        for ticket in sorted_today_events:
                            print(", ".join(ticket))

                    remove_today_events = input("remove today's events from the queue? (y/n): ")
                    if remove_today_events.lower() == 'y':
                        special_queue = [(ev_id, ev_date) for ev_id, ev_date in special_queue if ev_date != input_date]
                        print('tickets are removed from the queue')
                    else:
                        print("no tickets are found for today s event")
                    break
    
            else: # case 3 if the input date doesnt correspond to the special date:
                print("no tickets are found for today s event")
        
    return special_queue
#special_queue = todayEvents(tickets_list, special_queue)  


# Admin Menu #
#------------#

def display_admin_menu():
    print("Admin Menu:")
    print("1. Display Statistics")
    print("2. Book a Ticket")
    print("3. Display all Ticket")
    print("4. Change Ticket's Priority")
    print("5. Disable Ticket")
    print("6. Run Events")
    print("7. Exist")

def adminMenu():
    global current_date
    display_admin_menu()
    choice = int(input('please enter your choice here: '))

    while True:
        
        if choice == 1:
            max_event_id, max_event_count = displayStatistics(tickets_list)
            print(f'Max event id: {max_event_id}, {max_event_count}')
        
        elif choice == 2:
            username = input('enter a name: ')
            event_id = input('enetr the event id: ')
            priority = input('enter priority lvl from 0 to 3: ')

            current_date = get_date()
            new_ticket_id = new_ticket()

            new_ticket_list = f"{new_ticket_id}, {event_id}, {username}, {current_date}, {priority}\n"

            with open('ticket_list.txt', 'a') as file:
                file.write(new_ticket_list)

            tickets_list.append(new_ticket_list.strip().split(", "))
            print('ticket list updated')
        
        elif choice == 3:
            today_ticket = get_date()
            sorted_tickets = sort_tickets(tickets_list)
            print("today s tickets:")
            for ticket in sorted_tickets:
                if ticket[3] == today_ticket:
                    print(", ".join(ticket))

        elif choice == 4:
            ticket_to_change = input("enter the ticket id: ")
            new_priority = input("enter priority lvl from 0 to 3: ")
            change_priority(tickets_list, ticket_to_change, new_priority)

            for ticket in tickets_list:
                print(", ".join(ticket))

        elif choice == 5:
            tick_to_remove = input('enter the ticket id to remove: ')
            remove_tickets(tickets_list, tick_to_remove)
        
        elif choice == 6:
            special_queue = todayEvents(tickets_list, special_queue)  
        
        elif choice == 7: # ask the admin if he wants to save the changes 
            save_changes = input('save changes? (y/n): ')
            if save_changes == 'y':
                # saving the ticket list 
                with open('ticket_list.txt', 'w') as file:
                    for ticket in tickets_list:
                        file.write(", ".join(ticket) + '\n')
                
                # saving the special queue:
                with open('specia_queue.txt', 'w') as file:
                    for event_id, event_date, in special_queue:
                        file.write(f"{event_id}, {event_date}\n")
                print("changes saved!")
                break
        else:
            print('invlid key, try again')

        display_admin_menu()
        choice = int(input('please enter your choice here: '))
    return special_queue
##########
###user###
##########


def normal_user_name():
    normal_name = input("enter your name: ")
    return normal_name


def user_add_ticket():
    event_id = input('enter the event id: ')
    username2 = normal_user_name()
    current_date = get_date()
    priority = '0'

    new_tickets_id = new_ticket()
    new_ticket_list = f"{new_tickets_id}, {event_id}, {username2}, {current_date}, {priority}"

    with open('ticket_list.txt', 'a') as file:
        file.write(new_ticket_list)
    tickets_list.append(new_ticket_list.strip().split(", "))
    print("ticket added")


#-----------#
##user menu##
#-----------#

def display_user_menu():
    print("user menu:")
    print("1. add ticket")
    print("2. Save and Exit")

def userMenu():    

    while True:

        display_user_menu()
        choice = int(input('please enter your choice here: '))
        if choice == 1:
            user_add_ticket()
        elif choice == 2:
            with open('ticket_list.txt', 'w') as file:
                for ticket in tickets_list:
                    file.write(", ".join(ticket) + '\n')
            print('changes saved')
            break
        
        else:
            print('wrong choise, plz repeat')

#############
#log-in menu#
#############

def display_login_menu():
    username = input('enter the username: ')
    password = input('enter the password: ')

    if username == 'admin' and password == 'admin123123':
        adminMenu()
    else:
        userMenu()

display_login_menu()