from exercises_XP import Dog
import random

class PetDog(Dog):
    def __init__(self, *args, trained=False):
        super().__init__(*args)
        self.trained = trained

    def train(self):
        print(super().bark())
        self.trained = True

    def play(self, *args):
        print(f'{self.name} is playing with {args}')

    def do_a_trick(self):
        triks = ['does a barrel roll', 'stands on his back legs', 'shakes your hand', 'plays dead']
        if self.trained:
            print(f'{self.name} is {triks[random.randint(0, 3)]}')   
        else: 
            print(f'{self.name} is untrained')    

if __name__ == "__main__":
    dog1 = PetDog('Dok', 5, 30)
    dog2 = PetDog('Lenny', 7, 20)
    dog3 = PetDog('Rikky', 4, 25)
    dog1.train()
    dog2.train()
    dog1.do_a_trick()
    dog1.play(dog2.name)
    dog2.play(dog1.name, dog3.name)
    dog3.play(dog2.name)
    dog3.do_a_trick()
    dog2.do_a_trick()
    dog3.train()
    dog3.do_a_trick()
    print("\nexercise 3 done\n______________________")