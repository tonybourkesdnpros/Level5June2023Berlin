# Variables

## Simple, Complex

### Integers

vlan = 2**12

### Strings

fake_out = 1

fake_out_2 = '2'

x = fake_out + int(fake_out_2)


### Booleans

thing = True
other_thing = False


# Complex Data Structure

## Lists and Dictionaries

### List
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

# for item in planets:
#     print(item)

### Dictionary

starships = {'1701': {
                'name': 'Enterprise',
                'Captain': 'Kirk'},
             '1864': {
                'name': 'Reliant',
                'Captain': 'Khan'},
             '74656': {
                'name': 'Voyager',
                'Captain': 'Janeway'},
             '1031': {
                'name': 'Discovery',
                'Captain': 'Burnam'
             }}

# for ncc in starships:
#     print("NCC-"+ncc, "is the starship", starships[ncc]['name'], "and is commanded by Captain", starships[ncc]['Captain'])


def add_num(x, y):
   result = x + y
   return result

z = add_num(35, 5)

print(z)