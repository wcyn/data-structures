# https://www.interviewcake.com/question/python/mesh-message?course=fc1&section=trees-graphs
# You wrote a trendy new messaging app, MeshMessage, to get around flaky cell phone coverage.
#
# Instead of routing texts through cell towers, your app sends messages via the phones of nearby users,
# passing each message along from one phone to the next until it reaches the intended recipient.
# (Don't worry—the messages are encrypted while they're in transit.)
#
# Some friends have been using your service, and they're complaining
# that it takes a long time for messages to get delivered. After some preliminary debugging,
# you suspect messages might not be taking the most direct route from the sender to the recipient.
#
# Given information about active users on the network, find the shortest route for a
# message from one user (the sender) to another (the recipient).
# Return a list of users that make up this route.

from collections import deque


network = {
    "Min": ["William", "Jayden", "Omar"],
    "William": ["Min", "Noam"],
    "Jayden": ["Min", "Amelia", "Ren", "Noam"],
    "Ren": ["Jayden", "Omar"],
    "Amelia": ["Jayden", "Adam", "Miguel"],
    "Adam": ["Amelia", "Miguel", "Sofia", "Lucas"],
    "Miguel": ["Amelia", "Adam", "Liam", "Nathan"],
    "Noam": ["Nathan", "Jayden", "William"],
    "Omar": ["Ren", "Min", "Scott"]
}


class GraphNode:
    def __init__(self, label, neighbours=set()):
        self.label = label
        self.neighbours = neighbours


# graph = [GraphNode(label, set(network[label])) for label in network]
#
# print([(n.label, n.neighbours) for n in graph])


def get_shortest_path_bfs(graph, start_node, end_node):
    paths_to_visit = deque([start_node])
    # visited = {start_node}
    paths = {start_node: None}
    if not graph.get(start_node) or not graph.get(end_node):
        raise ValueError("Sender or Recipient is not in the Network")

    while paths_to_visit:
        current_node = paths_to_visit.popleft()
        if current_node == end_node:
            print(paths)
            return get_path(paths, current_node)

        for node in graph.get(current_node, []):
            if node not in paths:
                paths[node] = current_node
                paths_to_visit.append(node)
        # visited.add(current_node)
    return None


def get_path(path_map, node):
    node = path_map[node]
    path = [node]
    while node:
        path.append(node)
        node = path_map[node]
    return path


print(get_shortest_path_bfs(network, "Min", "Adam"))
