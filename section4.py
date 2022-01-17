class PlayerCharacter:
    membership = True # can't be modified

    def __init__(self, name='anonimus', age=0):
        if (age > 18):
            self.name = name
            self.age = age

    def run(self):
        print('run')

    def shout(self):
        print(f'my name is {self.name} member: {self.membership}')

player1 = PlayerCharacter('ironman', 23)
player2 = PlayerCharacter('ariandel', 23)
player2.attack = 90

print(player2.attack)
print(player1.age)
print(player2.shout())