import os #more language agnostic than "\n\n" per stackoverflow

#todo make a list from the data
#sort the list into groups of elves/calories
#sort by number high to low
#find the highest number of calories
#find the total of the three hightest calories

#use 'with' to auto close the file
#open the file called 'realdata.in' to something called 'f'
with open('day_one.in') as f:
    #take the data, assign a var 'data' = read the file, take out the spaces and commas, ett. split it where there is an empty line
    data = f.read().strip().split(os.linesep + os.linesep)

print(data) #test the data var 

each_elf = [ ] #cals for each elf #this works

for elf in data:
    calories = sum(map(int, elf.splitlines()))
    each_elf.append(calories) 

print(each_elf) #test split into each elf
print(type(each_elf)) #make sure it's a list
print(type(each_elf[1])) #make sure it's an int

#use sorted over sort idk why sort doesn't work here
each_elf_sorted = sorted(each_elf)
print(each_elf_sorted) #test the order from low to high

#print the last item in the list (most calories)
print(f"The elf with the most calories has {each_elf_sorted[-1]} calories")
#print the sum of three higest calories 
print(f"The total calories for the Top Three Elves is: {sum(each_elf_sorted[-3:])}")  
