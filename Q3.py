import networkx as nx
import numpy as np

#creator: Gil Matsliah, 312480791

class Worker:
    name: str
    # Worker name, for display.
    preferences: list
    # preferences[0] is the best shift for the worker.
    # preferences[1] is the 2nd-best shift for the worker. etc...
    current_shift: int
    # The shift to which the worker is currently assigned
    def __init__(self, name, preferences, current_shift):
        self.name = name
        self.preferences = preferences
        self.current_shift = current_shift

#build weighted graph with networkx to represent the working schedule and preferences
def build_graph(workers: list):
    graph = nx.DiGraph()
    for i in range(len(workers)):
        for j in workers[i].preferences:
            graph.add_edge(workers[i].current_shift, j, weight=j)
    return graph

#changing work schedule using top trading cycle algorithm and networkx dfs based find_cycle
def change_and_remove(graph, first):
    for i in list(nx.find_cycle(graph, first)):
        worker_name = ""
        for j in workers:
            if i[0] == j.current_shift:
                worker_name = j.name
        #printing changes and removing changed nodes from graph
        print(worker_name + " moves from shift " + str(i[0]) + " to shift " + str(i[1]))
        graph.remove_node(i[0])
    return

def exchange_shifts(workers: list):
    graph = build_graph(workers)
    while graph.number_of_nodes() > 0:
        first = np.random.choice(graph.nodes())
        if graph.number_of_nodes() == 1:
            print(str(workers[first].name) + " moves from shift " + str(workers[first].current_shift) + " to shift " + str(workers[first].current_shift))
            return
        change_and_remove(graph, first)
    return