import re

INPUT = 540391
INPUT_STR = '540391'
recipes = '37'
p1 = 0
p2 = 1


while INPUT_STR not in recipes[-7:]:
    # make the new recipes
    recipes += str(int(recipes[p1] + recipes[p2]))
    #update the positions
    p1 = (p1 + int(recipes[p1]) + 1) % len(recipes)
    p2 = (p2 + int(recipes[p2]) + 1) % len(recipes)
    print(len(recipes))
    
print("Part 1: ", recipes[INPUT:INPUT+10], "Part 2: ", recipes.index(INPUT_STR))