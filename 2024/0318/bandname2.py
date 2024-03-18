from random import choice

# 내가 짠것
# color_file = open('color.txt', 'r')
# color_lines = color_file.readlines()
# color = color_lines[random.randint(0, len(color_lines) - 1)]
#
# food_file = open('food.txt', 'r')
# food_lines = food_file.readlines()
# food = food_lines[random.randint(0, len(food_lines) - 1)]
#
# print(f"{color.replace('\n', '')} {food.replace('\n', '')}")

# 답지
color = open('txt_file/color.txt', 'r').read().split()
food = open('txt_file/food.txt', 'r').read().split()

print(f"{choice(color)} {choice(food)}")
