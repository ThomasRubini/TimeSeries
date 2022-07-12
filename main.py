from score import get_score, COLUMNS

# NB to ourselves : The group needs to be included in the database, not otherwise

def isInside(substr, str):
    for letter in substr:
        if not letter in str:
            return False
    return True

def semi_union(A, B):
    # "If we have a common prefix and the last character of A is small than the last character of B"
    if A[:-1] == B[:-1] and A[-1] < B[-1]:
        return A+B[-1]
    else:
        return None


# Fill the space
def fill_space_values(space, DB):
    for group in space.keys():
        space[group] = get_score(group)
    # for db_word in DB:
    #     for group in space.keys():
    #         if isInside(group, db_word):
    #             space[group]+=1


def generate_next_level(current_space, DB):
    next_space = {}

    # For each combination
    current_space_groups = list(current_space.keys())
    for i in range(len(current_space_groups)):
        for j in range(i+1, len(current_space_groups)):
    
            x = current_space_groups[i]
            y = current_space_groups[j]

            new_group = semi_union(x, y)
            if new_group == None: #Si on ne peut plus continuer les semi union, on passe a la valeur suivante
                break
            else:
                next_space[new_group] = 0

    
    fill_space_values(next_space, DB)
    
    return next_space

# generate len(word) words with one letter removed each time
def generate_cut_words(word):
    for letter_index in range(len(word)):
        yield word[:letter_index]+word[letter_index+1:]


# Generate all possibilities
def loop_generation(L, DB):

    # We put in the first level and we calculate the probabilities
    levels = [{i:0 for i in L}]
    #fill_space_values(levels[0], DB)

    # We generate the next two levels

    levels.append(generate_next_level(levels[-1], DB))
    levels.append(generate_next_level(levels[-1], DB))
    levels.append(generate_next_level(levels[-1], DB))
    
    levels.pop(0)
    
    while True:
        for first_level in levels[2]: # level i elements
            for second_level in generate_cut_words(first_level): # level i-1 elements
                
                first_comp = levels[2][first_level]<=levels[1][second_level] # f(X\a) <= f(x)

                for third_level in generate_cut_words(second_level): # level i-2 elements

                    second_comp = levels[1][second_level]<=levels[0][third_level] # f(x) <= f(Xub)

                    # if the two comparisons aren't equals
                    # if f(X\a) <= f(x) != f(x) <= (Xub)
                    if first_comp != second_comp:
                        print("\nINVALID GROUP PROBABILITIES DETECTED :")
                        print("groups :")
                        print(first_level, second_level, third_level)
                        print("probabilities :")
                        print(levels[2][first_level], levels[1][second_level], levels[0][third_level])
                        print("Stopping loop")
                        return False

        levels.append(generate_next_level(levels[-1], DB))
        levels.pop(0)


        if len(levels[-1])==0:
           return True    
    


DB = ["BCDE", "ABC", "ABF", "CDE", "ACD", "AEF"]

L = list(COLUMNS)





LSortie = loop_generation(L, DB) 
print("Return value :", LSortie)
