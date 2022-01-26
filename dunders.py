class Toy():
    def __init__(self,color,age):
        self.color = color
        self.age = age

    def __str__(self):
        return f'{self.color}'

    def __len__(self):
        return 5

    def __del__(self):
        print('deleted')

    def __call__(self):
        return('yesss')

action_figure = Toy('Red', 0)

print(action_figure.__str__())
print(len(action_figure))
print(action_figure())