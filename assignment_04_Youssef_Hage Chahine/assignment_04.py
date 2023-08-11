class Graph:
    
    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = []
    
    def add_edge(self, start, end):
        self.vertices[start].append(end)
        self.vertices[end].append(start)
    
    def remove_user(self, user):
        if user in self.vertices:
            for friend in self.vertices[user]:
                self.vertices[friend].remove(user)
            self.vertices.pop(user)
        else:
            print('user not found')

    def send_friend_request(self, user1, user2):
        if user1 in self.vertices and user2 in self.vertices:
            self.add_edge(user1, user2)
            print(f"friend request sent from {user1} to {user2}")
        else:
            print('users not found')

    def remove_friend(self, user1, user2):
        if user1 in self.vertices and user2 in self.vertices:
            if user2 in self.vertices[user1]:
                self.vertices[user1].remove(user2)
                self.vertices[user2].remove(user1)
                print(f"{user1} and {user2} are not friend")
            else:
                print(f"{user2} is not friend with {user1}")
        else:
            print("users are not found")
    

    def view_friend(self, user):
        if user in self.vertices:
            friend = self.vertices[user]
            if friend:
                print(f"friends of {user}: {','.join(friend)}")
            else:
                print(f"{user} forever alone")
        else:
            print("user not found")



class User:
    def __init__(self, username):
        self.username = username


def displayMenu():
    print("1. add a user")
    print("2. remove a user")
    print("3. send friend request")
    print("4. remove friend")
    print("5. list of friend")
    print("6. list of user in the platform")
    print("7. exit")

    

def Menu():
    social_media = Graph()

    displayMenu()
    choice = int(input('enter your choice: '))
    
    while choice != 7:

        if choice == 1:
            username = input("enter a username: ")
            if username in social_media.vertices:
                print("username already exists please enter a new one")
            else:
                social_media.add_vertex(username)
                print(f"user {username} has been added")
        
        elif choice == 2:
            username = input("enter the username to remove: ")
            social_media.remove_user(username)
            print(f"user {username} has been removed from the platform")
        
        elif choice == 3:
            user1 = input('enter your username: ')
            user2 = input('enter the username to send friend request: ')
            social_media.send_friend_request(user1, user2)
        
        elif choice == 4:
            user1 = input('enter your username: ')
            user2 = input('enter the username to remove: ')
            social_media.remove_friend(user1, user2)
        
        elif choice == 5:
            user = input("enter username")
            social_media.view_friend(user)
        
        elif choice == 6:
            
        else:
            print("invalid choice")
        
        print("----------")

        displayMenu()
        choice = int(input('enter your choice: '))

    print("bye!")    

Menu()

