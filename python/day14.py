
INPUT = 540391
in_as_list = [5, 4, 0, 3, 9, 1]
recipes = [3, 7]
positions = (0, 1)

while True:
    # make the new recipes
    new_score = recipes[positions[0]] + recipes[positions[1]]
    if new_score >= 10:
        new_score = [new_score//10, new_score%10]
        recipes.extend(new_score)
    else:
        recipes.append(new_score)
    #update the positions
    positions = tuple(map(lambda p: (recipes[p] + 1 + p)%len(recipes), positions))
    # part 1
    if len(recipes) >= INPUT + 10:
        part_1 = ''.join(map(str, recipes[INPUT:INPUT+10]))
        break
    
print(part_1)