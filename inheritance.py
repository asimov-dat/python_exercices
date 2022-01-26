class User:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged in')
    

class Wizard(User):
    def __init__(self,name,power,email):
        User.__init__(self,email)
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __init__(self,name,number_arrows,email):
        super().__init__(email)
        self.name = name
        self.number_arrows = number_arrows
    
    def attack(self):
        print(f'number of arrows: {self.number_arrows}')


wizard1 = Wizard('bitch',60, 'bitch@gmail.com')
archer = Archer('robin',100,'robin@outlook.com')

#introspection
print(dir(wizard1))

print(wizard1.email)
print(archer.email)