def matrix_print(board): 
    for innerList in board: 
        for elem in innerList: 
            print(str(elem) + " ", end ='')
        print("") 

def take_input(msg):
    # the data is in form [[1,2,3], [4,5,6], [7,8,_]] where _ is the blank tile
    print(msg)
    data = []
    for x in range(3):
        row = input().split(" ")
        data.append(row)
    return data


def puzzle(current, goal, level):
    # check if the current state is the goal state
    if current == goal:
        return True

    # if max depth is reached, return false
    if level == 3:
        return False

    # current possition of the blank tile
    blank_pos = None
    for x in range(3):
            for y in range(3):
                if current[x][y] == "_":
                    blank_pos = [x, y]
                    break

    # generate the possible moves from the current state
    def generate_moves(x, y):
        moves = []
        if x > 0:
            moves.append((x-1, y))
        if x < 2:
            moves.append((x+1, y))
        if y > 0:
            moves.append((x, y-1))
        if y < 2:
            moves.append((x, y+1))
        return moves
    
    # generate new states from the current state
    children_states = []
    for move in generate_moves(blank_pos[0], blank_pos[1]):
        # make a copy of the current state
        new_state = [row[:] for row in current]
        
        # swap the blank tile with the tile in the move
        new_state[blank_pos[0]][blank_pos[1]] = new_state[move[0]][move[1]]
        new_state[move[0]][move[1]] = "_"
        
        # calculate total state difference (Heuristic)
        h = 0
        for x in range(3):
            for y in range(3):
                if new_state[x][y] != goal[x][y] and new_state[x][y] != "_":
                    h += 1
        f = level+ h

        # add the new state along with heuristic to the children_states
        children_states.append((new_state, f))
    
    # select the best state from the children_states and call the function again
    children_states.sort(key=lambda x: x[1])
    
    # traverse all the children states
    for child in children_states:
        if puzzle(child[0], goal, level+1):
                matrix_print(child[0])
                print("\n  🡩  \n")
                return True

if __name__ == "__main__":
    # import start and goal states from user
    start = take_input("\nEnter start state: ")
    goal = take_input("\nEnter goal state: ")

    # call the solver function 
    print("\nSteps to solve: ")
    puzzle(start, goal, 0)
    matrix_print(start)
