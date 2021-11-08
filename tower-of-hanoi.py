def tower_of_hanoi(n , source,  auxiliary, destination):
    if n==1:
        print("Move disk 1 from ",source,"to ",destination)
        return
    tower_of_hanoi(n-1, source, destination, auxiliary)
    print("Move disk",n,"from ",source,"to ",destination)
    tower_of_hanoi(n-1, auxiliary, source,  destination)

if __name__ == "__main__":
    number_of_rings = int(input("Enter number of rings: "))
    tower_of_hanoi(number_of_rings, "A", "B", "C" )