class Dog:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age

poodle = Dog('poodle', 4)
bulldog = Dog('bulldog', 5)

print('poodle is a', poodle.species)
print('poodle is', poodle.age,'years old')
print('bulldog is a', bulldog.species)
print('bulldog is', bulldog.age,'years old')