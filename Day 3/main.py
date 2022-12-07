#read the data file
# #iterate it like the other days
with open('data.in', 'r') as f: #opens data file, reads it, auto closes data file
    each_rucksack = [i for i in f.read().strip().split("\n")]
#test each_rucksack to make sure it's a list    
#print(each_rucksack)    
#REDUCE THIS INTO FEWER LINES
#MAKE IT A F(X)
    total = 0
    for ruck_sack in each_rucksack:    
    #use a test array
        # test_array = 'vJrwpWtwJgWrhcsFMMfFFhFp'
        #find the mid point of the array
        middle_of_array = len(ruck_sack)// 2
        #prints middle_of_array
        # print(f"{middle_of_array} is the middle spot")
        #splits off the first half of the array
        first_half = ruck_sack[:middle_of_array]
        # print(first_half)
        #splits off the second half of the array
        second_half = ruck_sack[middle_of_array:]
        # print(second_half)
        char_total = 0
# COMPARE THE TWO ARRAYS, FIND THE COMMON CHAR
        #iterate through each first_half and second_half, find the common character
        common_char = [i for i in first_half if i in second_half]
        #print the common char
        one_char = common_char[0]
        value = ord(one_char) - 96 if one_char.islower() else ord(one_char) -64 + 26
        total += value
print(f"The total of the first part is {total}.")        

rucksack_lines = 0
part_two_total = 0
while rucksack_lines < len(each_rucksack):
    rucksack_1 = each_rucksack[rucksack_lines]
    rucksack_2 = each_rucksack[rucksack_lines +1]
    rucksack_3 = each_rucksack[rucksack_lines +2]
    for item in rucksack_1:
        if item in rucksack_2 and item in rucksack_3:
            value_2 = ord(item) - 96 if item.islower() else ord(item) -64 + 26
            part_two_total += value_2
            rucksack_lines += 3
            break

print(f"The total of the second part is {part_two_total}.")