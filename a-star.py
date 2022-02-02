class Node():
    def __init__(self, graph, vertex, gval, fval, parent ):
        self.graph = graph
        self.vertex = vertex
        self.gval = gval
        self.fval = fval
        self.parent = parent

    def generate_child(self):
        children = []
        for child_vertex in range(0, len(self.graph)):
            if self.graph[self.vertex][child_vertex] != 0:
                g = self.gval + self.graph[self.vertex][child_vertex]
                child = Node(self.graph, child_vertex, g, 0, self)
                children.append(child)
        return children

class aStarSearch():
    def __init__(self, graph, heuristics, start_vertex, stop_vertex):
        self.graph = graph
        self.heuristics = heuristics
        self.start_vertex = start_vertex
        self.stop_vertex = stop_vertex
        self.open = []
        self.closed = []
    
    def process(self):
        # create start node
        start = Node(self.graph, self.start_vertex,0, 0, None)

        # place the start node on open list
        self.open.append(start)

        # start traversing all states
        while len(self.open) > 0:
            
            #get the first item from open list
            cur = self.open[0]

            # if goal state found and print the state and break the loop
            if cur.vertex == self.stop_vertex:
                sol = [cur.vertex]
                ptr = cur.parent
                while ptr != None:
                    sol.append(ptr.vertex)
                    ptr = ptr.parent
                print(sol[::-1])
                break 

            # generate all the children
            for child in cur.generate_child():

                    # check if child is in closed list
                    isValid = True
                    for old_child in self.closed:
                        if old_child.vertex == child.vertex:
                            isValid = False
                            break
                            
                    if isValid:
                        child.fval = child.gval + self.heuristics[child.vertex]
                        self.open.append(child)
            
            # delete the cur in open list and add it to closed list
            self.closed.append(cur)
            del self.open[0]

            # sort the open list based on fval
            self.open.sort(key = lambda x:x.fval,reverse=False)

if __name__ == "__main__":
    graph = [[0, 2, 9, 4],
             [2, 0, 2, 9],
             [9, 2, 0, 2],
             [4, 9, 2, 0]]
    heuristics = [9, 2, 0, 2] #estimate from that vertex till goal
    algo = aStarSearch(graph, heuristics, 0, 2)
    algo.process()
