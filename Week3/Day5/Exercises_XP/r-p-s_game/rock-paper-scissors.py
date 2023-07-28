from game import Game

color_reset = '\033[0m'  
color_cyan = '\033[36m'
color_magenta = '\033[35m'

def get_user_menu_choice() :
    user_input_list = ['x', 'g', 's']
    print('_______________\nMenu\n(g) Play a new game \n(s) Show scores\n(x) Exit\n' )
    try:
        user_input = input('Input your choice: ')
        if user_input not in user_input_list:
            raise Exception ('')
        elif user_input == 'g' :
            return user_input
        elif user_input == 'x' : 
            return user_input
        else:
            return user_input 
    except Exception as err:
        print(err)                     

def print_results(results) :
    result = {'draw' : 0, "win" : 0, "loss" : 0}
    for r in results:
        for key, value in r.items():
            result[key] += value
    print(f"{color_cyan}You win {color_magenta}{result['win']}{ color_reset}{color_cyan} times, loss {color_magenta}{result['loss']}{color_reset}{color_cyan} times and {color_magenta}{result['draw']}{color_reset}{color_cyan} times were draw{color_reset}")

def main() :
    all_results = []
    user_choice = ''
    while user_choice != 'x':
        user_choice = get_user_menu_choice()
        if user_choice == 'g':
            a = Game()
            result = a.play()
            all_results.append(result)                
        else:
            print_results(all_results)

main()