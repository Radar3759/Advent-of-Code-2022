
with open('data.in', 'r') as f: #opens data file, reads it, auto closes data file
    rounds = [i for i in f.read().strip().split("\n")]

#test data to see if it looks like it should 'A X'
print(rounds)
#YOU are column TWO
total_score = 0 #figure out why this made it work
for round in rounds:
    my_score = 0
    opp_game = round[0] #don't forget this step next time
    my_game = round[2]   
    
    if my_game == 'X':
        # my_score += 1 #tidy it by removing these
        if opp_game == 'A':
            my_score += 4
        elif opp_game == 'B':
            my_score += 1
        elif opp_game == 'C':
            my_score += 7
    elif my_game == 'Y':
        # my_score += 2
        if opp_game == 'A':
            my_score += 8
        elif opp_game == 'B':
            my_score += 5
        elif opp_game == 'C':
            my_score += 2
    elif my_game == 'Z':
        # my_score += 3
        if opp_game == 'A':
            my_score += 3
        elif opp_game == 'B':
            my_score += 9
        elif opp_game == 'C':
            my_score += 6
    total_score += my_score #order is IMPORTANT here
print(f"The total score for you: {total_score}")