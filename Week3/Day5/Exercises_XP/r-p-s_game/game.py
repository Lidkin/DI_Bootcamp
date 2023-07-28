from random import choice

class Game:
    choice_list = ["rock", "paper", "scissors"]
    red = '\033[91m'
    green = '\033[92m'
    reset = '\033[0m'

    def __init__ (self):
       self.result = {'draw' : 0, "win" : 0, "loss" : 0}    

    @staticmethod
    def get_user_item():
        while True:
            try:
                user_choice = input("Choise rock(r) / papper(p) / scissors(s) : ")
                if user_choice[0] not in [word[0] for word in Game.choice_list] and user_choice not in Game.choice_list: 
                    raise Exception ("Wrong choice")
            except Exception as err:
                print(err)
            else:
                break
        return user_choice    

    @staticmethod
    def get_computer_item():
        return choice(Game.choice_list)

    def get_game_result(self, user, computer):
        if user == computer:
            self.result['draw'] += 1 
            print(f"Draw")
        elif (user == 's' and  computer == 'p') or (user == 'p' and computer == 'r') or (user == 'r' and computer == 's') :
            self.result['win'] += 1 
            print(f"{Game.green}You win{Game.reset}")
        else:
            self.result['loss'] += 1  
            print(f"{Game.red}You loss{Game.reset}")
        return self.result                   

    def play(self):
        user = self.get_user_item()
        computer = self.get_computer_item()
        result = self.get_game_result(user[0], computer[0])
        return result