from collections import deque
class Node():
    def __init__(self, state, capacity ):
        self.state = state
        self.capacity = capacity

    def generate_child(self):
        A, B = self.state[0], self.state[1]
        ACap, BCap = self.capacity[0], self.capacity[1]

        children = set()
        # fill all A jug 
        children.add((ACap, B))

        # fill all B jug
        children.add((A, BCap))

        # empty jug A
        children.add((0, B))

        # empty jug B
        children.add((A, 0))

        # fill jug A by emptying jug B
        if A + B <= ACap:
            children.add((A+B, 0))
        
        # fill jug B by emptying jug A
        if A + B <= BCap:
            children.add((0, A+B))
        
        # Pour some water from B jug to fill A jug
        if B-(ACap-A) <= BCap and B-(ACap-A) >= 0:
            children.add((ACap, B-(ACap-A)))

        # Pour some water from A jug to fill B jug
        if A-(BCap-B) <= ACap and A-(BCap-B) >= 0:
            children.add((A-(BCap-B), BCap))

        return children


class waterJugBFS():
    def __init__(self, capacity, start, target):
        self.capacity = capacity
        self.start = start
        self.target = target
        self.closed = set()
        self.open = deque()
        self.path = []
    
    def process(self):
        # create start node and add it to open list
        start_state = Node(self.start, capacity)
        self.open.append(start_state)

        # start traversing all states
        while len(self.open) > 0:

            cur = self.open.popleft()
            self.path.append(cur.state)

           # if goal state found and print the state and break the loop
            if cur.state[0] == self.target or cur.state[1] == self.target:
                if (cur.state[0] == self.target):
                    if (cur.state[1] != 0): 
                        self.path.append([cur.state[0], 0])
                elif (cur.state[0] != 0): 
                    self.path.append([0, cur.state[1]])
                for i in range(len(self.path)):
                    print("(", self.path[i][0], ",", self.path[i][1], ")")
                break

            self.closed.add(cur.state)
            # generate all the children
            for child in cur.generate_child():
                if child not in self.closed:
                    self.open.append(Node(child, capacity))

if __name__ == "__main__":
    capacity = (3, 4) 
    start = (0, 0)
    target = 2
    puz = waterJugBFS(capacity, start, target)
    puz.process()
