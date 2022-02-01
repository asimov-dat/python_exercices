# class PlayerCharacter:
#     membership = True # can't be modified

#     def __init__(self, name='anonimus', age=0):
#         if (age > 18):
#             self.name = name
#             self.age = age

#     def run(self):
#         print('run')

#     def shout(self):
#         print(f'my name is {self.name} member: {self.membership}')

# player1 = PlayerCharacter('ironman', 23)
# player2 = PlayerCharacter('ariandel', 23)
# player2.attack = 90

# print(player2.attack)
# print(player1.age)
# print(player2.shout())

#-----------------------
# iterables, dictionaries, tuples, strings, list

user = {
    'name': 'golem',
    'age': 2323,
    'can_swim': False
}

for item in user.items():
    print(item)

for item in user.values():
    print(item)

for item in user.keys():
    print(item)

for key, value in user.items():
    print(key,':', value)