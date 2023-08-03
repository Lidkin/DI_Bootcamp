from menu_item import MenuItem as Menu
from menu_manager import MenuManager as Manager


def show_user_menu():
    options = ['View an Item (V)', 'Add an Item (A)', 'Delete an Item (D)', 'Update an Item (U)', 'Show the Menu (S)']
    user_menu = '\n'.join(options)
    print(user_menu)    

def view_item():
    try:    
        name = input('--Enter Item name: ')
        if len(name) > 30:
            raise Exception('must be shorter 30 characters')
        print(Manager.get_by_name(name))    
    except Exception as err:
        print(err) 

def add_item_to_menu():
    try:    
        name = input('--Enter Item name: ')
        if len(name) > 30:
            raise Exception('must be shorter 30 characters')
        price = int(input('--Enter Item price: '))
        if type(price) != int:
            raise Exception('must be integer')
        Menu(name, price).save()
    except Exception as err:
        print(err)  
    else:
        print('Item was added successfully.')   

def remove_item_from_menu():
    try:    
        name = input('--Enter Item name what you want to be deleted: ')
        item = Manager.get_by_name(name)
        Menu(item[0][1],item[0][2]).delete()
    except Exception as err:
        print(err)
    else:
        print('Delete was completed.')    

def update_item_from_menu():
    try:    
        name = input('--Enter Item name: ')
        if len(name) > 30:
            raise Exception('must be shorter 30 characters')
        price = int(input('--Enter item price: '))
        if type(price) != int:
            raise Exception('must be integer')
        Menu(name, price).update(name, price)
    except Exception as err:
        print(err)  
    else:
        print('Item was updated successfully.')    
           
def show_restaurant_menu():
    Manager.all()

def menu():
    choices = {'v': view_item, 'a': add_item_to_menu, 'd': remove_item_from_menu, 'u': update_item_from_menu, 's': show_restaurant_menu}
    show_user_menu()
    choice = ''
    while choice != 's':
        choice = input('Enter your choice: ').lower()
        choices[choice]()

menu()            
       