# Dijkstra's algorithm

graph = {}
graph["Start"] = {}
graph["Start"]["A"] = 6
graph["Start"]["B"] = 2

graph["A"] = {}
graph["A"]["Finish"] = 1

graph["B"] = {}
graph["B"]["A"] = 3
graph["B"]["Finish"] = 5

graph["Finish"] = {}


infinity = float("inf")
costs_from_start = {}
costs_from_start["A"] = 6
costs_from_start["B"] = 2
costs_from_start["Finish"] = infinity

parents = {}
parents["A"] = "Start"
parents["B"] = "Start"
parents["Finish"] = None

processed = []


def find_lowest_cost_node(costs_from_start):
    lowest_cost = float("inf")
    lowest_cost_node = None

    for node in costs_from_start:
        cost = costs_from_start[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node

    return lowest_cost_node


node = find_lowest_cost_node(costs_from_start)

while node is not None:
    lowest_cost = costs_from_start[node]
    neighbors = graph[node]

    for i in neighbors.keys():
        new_cost = lowest_cost + neighbors[i]

        if costs_from_start[i] > new_cost:
            costs_from_start[i] = new_cost
            parents[i] = node

    processed.append(node)
    node = find_lowest_cost_node(costs_from_start)


print(graph.keys())
print(graph["Start"].keys())
print("Cost from the start to each node:")
print(costs_from_start)