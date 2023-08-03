from manage_connection import manage_connection as mc

class MenuItem:
    def __init__(self, name, price = 0):
        self.name = name
        self.price = price

    def save(self):
        query = f"""
                INSERT INTO menu_items (item_name, item_price)
                VALUES {(self.name,self.price)}
                """
        return mc(query, "insert")

    def delete(self):
        query = f"""
        delete from menu_items
        where item_name = '{self.name}' and item_price = '{self.price}';
        """
        return mc(query, 'delete')

    def update(self, new_name, new_price):
        query = f'''
        update menu_items set item_name = '{new_name}', item_price = {new_price}
        where item_name = '{self.name}' and item_price = {self.price}
        '''    
        return mc(query, 'update')
              