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

class User:
    def __init__(self, username):
        self.username = username