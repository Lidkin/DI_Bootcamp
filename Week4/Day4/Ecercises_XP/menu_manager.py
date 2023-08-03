from manage_connection import manage_connection as mc
from menu_item import MenuItem as Menu

class MenuManager(Menu):
    @staticmethod     
    def get_by_name(name):
        query = f'''
        select * from menu_items
        where item_name = '{name}'
        '''
        return mc(query, 'select')
    
    @staticmethod
    def all():
        query = f'''
        select * from menu_items
        '''
        print(mc(query, 'select'))     