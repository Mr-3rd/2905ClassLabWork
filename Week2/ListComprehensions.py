strings = ['pizza', 'steak', 'taco']
lengths = [len(string) for string in strings]

print(lengths)

numbers = [1, 40, 300, 22000]
tripled_numbers = [n * 3 for n in numbers]
print(tripled_numbers)

string_numbers = numbers = ["1", "40", "300", "22000"]
int_numbers = [int(string2) for string2 in string_numbers]
print(int_numbers)

my_turn = [2, 4, 6]
add_one = [num + 1 for num in my_turn]
print(add_one)

numbers2 = [1, 40, 300, -500, -6, 10, 30]
negative_numbers = [n for n in numbers2 if n < 0]
print(negative_numbers)

foods = ['cheese pizza', 'steak', 'taco', 'peperoni pizza']
pizzas = [food for food in foods if 'pizza' in food]
print(pizzas)

example = [2, 4, 6]

one_in_example = 1 in example
two_in_example = 2 in example
print(f'{one_in_example} | {two_in_example}')

course = "A360 University"
if 'A360' in course:
    print("Automation Anywhere University")

# my turn

my_numbers = [0, 3, 4, 0, 22, 1]
nonzero_numbers = [n for n in my_numbers if n != 0]
print(nonzero_numbers)

classes = ['ITEC 2560', 'BTEC 1010', 'ITEC 2905']
ITEC_classes = [class1 for class1 in classes if 'ITEC' in class1]
print(ITEC_classes)

# alternative
only_itec = [c for c in classes if c.startswith('ITEC')]
print(only_itec)

# combining actions
foods = ['cheese pizza', 'steak', 'taco', 'peperoni pizza']
pizzas = [food.upper() for food in foods if 'pizza' in food]
print(pizzas)

my_numbers = [0, 10, 4, 0, 32]
nonzero_numbers = [n * 2 for n in my_numbers if n != 0]
print(nonzero_numbers)
