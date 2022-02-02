from itertools import permutations

def travellingSalesmanProblem(graph, source_city, no_of_cities):
 
    # store all vertex apart from source vertex
    vertices = []
    for i in range(no_of_cities):
        if i != source_city:
            vertices.append(i)
 
    # store minimum path length and order
    min_path_length = 999
    min_path_order = []

    for path_order in permutations(vertices):
 
        # store current Path weight(cost)
        current_path_length = 0
 
        # compute current path weight
        curr_city = source_city
        for next_city in path_order:
            current_path_length += graph[curr_city][next_city]
            curr_city = next_city
        
        # add the path back to source city
        current_path_length += graph[curr_city][source_city]
 
        # update minimum
        if current_path_length < min_path_length:
            min_path_length = current_path_length
            min_path_order = path_order

         
    return min_path_length, min_path_order
 
 
if __name__ == "__main__":
    graph = [[0, 10, 15, 20], [10, 0, 35, 25],
            [15, 35, 0, 30], [20, 25, 30, 0]]
    dis, order = travellingSalesmanProblem(graph, 0, len(graph))
    print("Distance : ", dis)
    print("Order: 0 ->", order, "-> 0")
