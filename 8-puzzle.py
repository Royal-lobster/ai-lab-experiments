class Node:
    def __init__(self,data,level,fval):
        self.data = data
        self.level = level
        self.fval = fval

    def generate_child(self):
        # find the blank possition in the current state
        blank_pos = None
        for x in range(3):
                for y in range(3):
                    if self.data[x][y] == "_":
                        blank_pos = [x, y]
                        break
        # find the possible moves
        moves = []
        x, y = blank_pos[0], blank_pos[1]
        if x > 0: moves.append((x-1, y))
        if x < 2: moves.append((x+1, y))
        if y > 0: moves.append((x, y-1))
        if y < 2: moves.append((x, y+1))
        
        children = []
        for move in moves:
            # generate child state for current move
            new_state = [row[:] for row in self.data]        
            new_state[blank_pos[0]][blank_pos[1]] = new_state[move[0]][move[1]]
            new_state[move[0]][move[1]] = "_"   

            # append the new state to children
            child_node = Node(new_state,self.level+1,0)
            children.append(child_node)

        return children

class Puzzle:
    def __init__(self,size):
        self.n = size
        self.open = []
        self.closed = []

    def take_input(self, msg):
        print(msg)
        data = []
        for x in range(3):
            row = input().split(" ")
            data.append(row)
        return data

    def f(self,start,goal):
        return self.h(start.data,goal) + start.level

    def h(self,start,goal):
        temp = 0
        for i in range(0,self.n):
            for j in range(0,self.n):
                if start[i][j] != goal[i][j] and start[i][j] != '_':
                    temp += 1
        return temp
        

    def process(self):
        # accept the start and goal states as input
        start = self.take_input("\nEnter start state: ")
        goal = self.take_input("\nEnter goal state: ")

        # make the start node
        start = Node(start,0,0)
        start.fval = self.f(start,goal)

        # place the start node in open list
        self.open.append(start)
        
        # start traversing all states
        print("\nSteps to solve : ")
        while True:
            print("\n  ￬  \n")

            # get the first item from open list
            cur = self.open[0]

            # print the current state
            for i in cur.data:
                for j in i:
                    print(j,end=" ")
                print("")

            # if the current state is goal state, break
            if(self.h(cur.data,goal) == 0):
                break

            # produce all child states and append to open list
            for child in cur.generate_child():
                child.fval = self.f(child,goal)
                self.open.append(child)

            # delete the current state in open list and add append it to closed list
            self.closed.append(cur)
            del self.open[0]

            # sort the open list based on fval
            self.open.sort(key = lambda x:x.fval,reverse=False)


if __name__ == "__main__":
    puz = Puzzle(3)
    puz.process()
