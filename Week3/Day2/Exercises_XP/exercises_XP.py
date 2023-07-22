#1_____________________________________________________
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'

if __name__ == "__main__":
    all_cats = [Bengal('Bengal', 3), Chartreux('Chartreux', 5), Siamese('Siamese', 7)]   
    sara_pets = Pets(all_cats)  
    sara_pets.walk() 
    print("\nexercise 1 done\n______________________")  

#2_____________________________________________________
class Dog():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f'{self.name} is barking'

    def run_speed(self):
        return self.weight/self.age*10

    def fight(self, other_dog):
        if self.run_speed() > other_dog.run_speed():
            return f'{self.name} is the winner'
        else:
            return f'{other_dog.name} is the winner'


if __name__ == "__main__":
    Dok = Dog('Dok', 5, 30)
    Lenny = Dog('Lenny', 7, 20)
    Rikky = Dog('Rikky', 4, 25)

    print(Dok.bark(), ", his speed: {:.2f}".format(Dok.run_speed()))
    print(Lenny.bark(), ", his speed: {:.2f}".format(Lenny.run_speed()))
    print(Rikky.bark(), ", his speed: {:.2f}".format(Rikky.run_speed()))

    print(f"Dok vs Lenny: ", Dok.fight(Lenny))
    print(f"Dok vs Rikky: ", Dok.fight(Rikky))
    print(f"Rikky vs Lenny: ", Lenny.fight(Rikky))
    print("\nexercise 2 done\n______________________")

#3_____________________________________________________
# dog.py
