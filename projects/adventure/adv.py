from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "projects/adventure/maps/test_line.txt"
# map_file = "projects/adventure/maps/test_cross.txt"
# map_file = "projects/adventure/maps/test_loop.txt"
# map_file = "projects/adventure/maps/test_loop_fork.txt"
map_file = "projects/adventure/maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

trackPrevRoom = [None]
dirOpposite = {'n': 's', 'e': 'w', 's': 'n', 'w': 'e'}
visited = {}
roomMaster = {}
# check each direction - dict_keys(['s', 'e', 'w'])
print(room_graph[6][1])


def possibleOptions(roomID):
    options = []
    if 'n' in room_graph[roomID][1].keys():
        options.append('n')
    if 'e' in room_graph[roomID][1].keys():
        options.append('e')
    if 's' in room_graph[roomID][1].keys():
        options.append('s')
    if 'w' in room_graph[roomID][1].keys():
        options.append('w')
    return options
while len(visited) < len(room_graph):
    roomID = player.current_room.id
    if roomID not in roomMaster:
        visited[roomID] = roomID
        roomMaster[roomID] = possibleOptions(roomID)

    if len(roomMaster[roomID]) < 1:
        prevRoom = trackPrevRoom.pop()
        traversal_path.append(prevRoom)
        player.travel(prevRoom)

    else:
        nextDirection = roomMaster[roomID].pop(0)
        traversal_path.append(nextDirection)
        trackPrevRoom.append(dirOpposite[nextDirection])
        player.travel(nextDirection)
# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# walk
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
