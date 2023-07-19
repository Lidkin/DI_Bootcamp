#1____________________________________________
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

def oldest_cat(cats):
    oldes_cat = None
    oldest = 0
    for cat in cats:
        if cat.age > oldest:
            oldest = cat.age
            oldes_cat = cat
    return oldes_cat

red_cat = Cat("Reddy", 3)    
brown_cat = Cat("Brownie", 5)   
white_cat = Cat("Snowball", 1) 
cats = (red_cat, brown_cat, white_cat)

print("The oldest cat is {0} and is {1} years old.".format(oldest_cat(cats).name, oldest_cat(cats).age))   

#2____________________________________________
class Dog:
    def __init__(self, dog_name, dog_height):
        self.name = dog_name
        self.height = dog_height

    def bark(self):
        print("{0} goes woof!".format(self.name))  

    def jump(self):
        print("{0} jumps {1} cm high!".format(self.name, self.height * 2))

davids_dog = Dog("Rex", 50)
print(f"David's dog name is {davids_dog.name} and it's height is {davids_dog.height}")
davids_dog.bark()
davids_dog.jump()

sarahs_dog = Dog("Teacup", 20)
print(f"Sarah's dog name is {sarahs_dog.name} and it's height is {sarahs_dog.height}")
sarahs_dog.bark()
sarahs_dog.jump()

if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name}")
else:
    print(f"{sarahs_dog.name}")    

#3____________________________________________
class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

stairway= Song(["There's a lady who's sure","all that glitters is gold", "and she's buying a stairway to heaven"])  
stairway.sing_me_a_song()

#4____________________________________________
class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_animal(self, new_animal):
        self.animals.append(new_animal)

    def get_animals(self):
        print(f'{self.name} has: {", ".join(self.animals)}')        

    def sell_animals(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold) 

    def sort_animals(self):
        sorted_animals = sorted(self.animals)
        grouped_animals = {}

        for animal in sorted_animals:
            first_letter = animal[0]

            if first_letter not in grouped_animals:
                grouped_animals[first_letter] = []

            grouped_animals[first_letter].append(animal)

        return grouped_animals

    def get_groups(self):
        grouped_animals = self.sort_animals()

        for letter, animals in grouped_animals.items():
            animals_string = ', '.join(animals)
            print(f'Animals starting with letter {letter}: {animals_string}')

ramat_gan_safari = Zoo("Ramat-Gan Safari")
ramat_gan_safari.add_animal("Baboon")   
ramat_gan_safari.add_animal("Emu")
ramat_gan_safari.add_animal("Giraffe")
ramat_gan_safari.add_animal("Crocodile")
ramat_gan_safari.add_animal("Tiger")
ramat_gan_safari.add_animal("Bear")
ramat_gan_safari.add_animal("Cougar")
ramat_gan_safari.add_animal("Gorilla")
ramat_gan_safari.get_animals()
ramat_gan_safari.sell_animals("Emu")
ramat_gan_safari.get_animals()
ramat_gan_safari.sort_animals()
ramat_gan_safari.get_groups()