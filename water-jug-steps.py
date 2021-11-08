# RULES =>
# 1. Fill the 4 gallon jug completely
# 2. Fill the 3 gallon jug completely
# 3. Empty the 4 gallon jug
# 4. Empty the 3 gallon jug
# 5. Pour some water from the 3 gallon jug to fill the four gallon jug
# 6. Pour some water from the 4 gallon jug to fill the three gallon jug
# 7. Pour all water from 3 gallon jug to the 4 gallon jug
# 8. Pour all water from 4 gallon jug to the 3 gallon jug

# SOLUTION STEPS =>
# 2, 9, 2, 7, 5, 9


if __name__ == "__main__":
    J4,J3 = 0,0
    print("initial state of the water jugs: ", "J4:",J4,"J3:",J3)
    while(J4 != 2):
        rule = int(input("enter rule number: "))
        if(rule == 1):
            # Fill the 4 gallon jug completely
            J4 = 4
        elif(rule == 2):
            # Fill the 3 gallon jug completely
            J3 = 3
        elif(rule == 3):
            # Empty the 4 gallon jug
            J4 = 0
        elif(rule == 4):
            # Empty the 3 gallon jug
            J3 = 0
        elif(rule == 5):
            # Pour some water from the 3 gallon jug to fill the four gallon jug
            J3 = J3-(4-J4)
            J4 = 4
        elif(rule == 6):
            # Pour some water from the 4 gallon jug to fill the three gallon jug
            J4 = J4-(3-J3)
            J3 = 3
        elif(rule == 7):
            # Pour all water from 3 gallon jug to the 4 gallon jug
            if(J4 + J3 < 4):
                J4 = J4 + J3
                J3 = 0
        elif(rule == 8):
            # Pour all water from 4 gallon jug to the 3 gallon jug
            if(J4 + J3 < 3):
                J3 = J4 + J3
                J4 = 0
        else:
            break
        print("J4:",J4,"J3:",J3)