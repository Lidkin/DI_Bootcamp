class Farm():
    def __init__(self, name):
        self.name = name
        self.animals = {}
        print(f"{self.name}'s farm", end="\n\n")

    def add_animal(self, animal, amount=0):
        self.animals.setdefault(animal, amount)
        if animal in self.animals and amount == 0:
            self.animals[animal] += 1

    def get_info(self):
        line = []
        for animal, amount in self.animals.items():
            line.append(f"{animal}: {amount}")
        string = "\n".join(line)    
        return f"{string}\n\n     E-I-E-I-0!"

    def get_animal_types(self):
        return sorted(list(self.animals.keys()))

    def get_short_info(self):
        sorted_animals = self.get_animal_types()  
        return "\nMcDonald's farm has {}s, {}s and {}.".format(sorted_animals[0], sorted_animals[1], sorted_animals[2])    

macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
print(macdonald.get_short_info())