# Sets

cars = set()  # create empty set
cars.add('500 Pop')
cars.add('Elantra GT')
print(cars)

cats = {'lion', 'tiger', 'Cat'}
cats.add('lion')
cats.add('cheetah')
print(cats)

for cat in cats:
    print(cat)

# removing duplicates
cat_list = ['lion', 'tiger', 'Cat', 'cheetah', 'tiger', 'Cat']
cat_list_no_duplicates = list(set(cat_list))
print(cat_list_no_duplicates)

try:
    print(cat_list_no_duplicates[10])
except:
    print('That cat does not exist')
