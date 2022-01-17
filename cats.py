#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('manolo', 23)
cat2 = Cat('pepa', 12)
cat3 = Cat('lupita', 4)


# 2 Create a function that finds the oldest cat

ages = [cat2, cat1, cat3]
ages.sort()
print(ages[-1])

def oldestCat(self,cat1,cat2,cat3):
    ages = [cat1.age, cat2.age, cat3.age]
    ages.sort()



# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2