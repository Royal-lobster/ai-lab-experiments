class Node():
    def __init__(self, graph, vertex, hval ):
        self.graph = graph
        self.vertex = vertex
        self.hval = hval

    def generate_child(self):
        children = []
        for child_vertex in range(0, len(self.graph)):
            if self.graph[self.vertex][child_vertex] != 0:
                child = Node(self.graph, child_vertex, 0)
                children.append(child)
        return children

class hillClimbSearch():
    def __init__(self, graph, heuristics, start_vertex, stop_vertex):
        self.graph = graph
        self.heuristics = heuristics
        self.start_vertex = start_vertex
        self.stop_vertex = stop_vertex
    
    def process(self):
        # create start node
        start = Node(self.graph, self.start_vertex,self.heuristics[self.start_vertex])

        # start traversing all states
        cur = start
        print("path from start to goal : ")
        while True:
            
            print(cur.vertex, end=" ")

            # if goal state found and print the state and break the loop
            if cur.vertex == self.stop_vertex:
                break 

            # generate all the children
            min_cost_child = None
            for child in cur.generate_child():
                child.hval = self.graph[cur.vertex][child.vertex]+self.heuristics[child.vertex]
                if min_cost_child == None or child.hval < min_cost_child.hval:
                    min_cost_child = child
            
            # make cur as min_cost_child
            cur = min_cost_child

if __name__ == "__main__":
    graph = [[0, 2, 9, 4],
             [2, 0, 2, 9],
             [9, 2, 0, 2],
             [4, 9, 2, 0]]
    heuristics = [9, 2, 0, 2] #estimate from that vertex till goal
    algo = hillClimbSearch(graph, heuristics, 0, 2)
    algo.process()
    print("")
