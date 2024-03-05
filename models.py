import sqlite3

class Schema:
    def __init__(self):
        self.conn = sqlite3.connect('restaurant.db')
        self.create_restaurant_table()


    def __del__(self):
        self.conn.commit()
        self.conn.close()


    def create_restaurant_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS "Restaurant" (
          id INTEGER PRIMARY KEY,
          Name TEXT NOT NULL,
          Dining_Type TEXT NOT NULL,
          Food_Type TEXT NOT NULL,
          Rating INTEGER NOT NULL
        );
        """
        self.conn.execute(query)


class RestaurantModel:
    TABLENAME = "Restaurant"

    def __init__(self):
        self.conn = sqlite3.connect('restaurant.db')
        self.conn.row_factory = sqlite3.Row


    def __del__(self):
        self.conn.commit()
        self.conn.close()


    def create(self, params):
        query = f'insert into {self.TABLENAME} ' \
                f'(Name, Dining_Type, Food_Type, Rating) ' \
                f'values ("{params.get("Name")}","{params.get("Dining_Type")}","{params.get("Food_Type")}","{params.get("Rating")}")'
        result = self.conn.execute(query)
        return self.get_by_id(result.lastrowid)


    def delete(self, restaurant_id):
        query = f"DELETE FROM {self.TABLENAME} WHERE id = {restaurant_id}"
        self.conn.execute(query)
        return self.list_restaurants()


    def update(self, item_id, update_dict):
        """
        column: value
        Title: new title
        """
        set_query = ", ".join([f'{column} = "{value}"'
                     for column, value in update_dict.items()])

        query = f"UPDATE {self.TABLENAME} " \
                f"SET {set_query} " \
                f"WHERE id = {item_id}"
    
        self.conn.execute(query)
        return self.get_by_id(item_id)


    def list_restaurants(self, where_clause=""):
        if where_clause == "":
            query = f"SELECT id, Name, Dining_Type, Food_Type, Rating FROM {self.TABLENAME}"
        else:
            query = f"SELECT id, Name, Dining_Type, Food_Type, Rating FROM {self.TABLENAME} {where_clause}"
        result_set = self.conn.execute(query).fetchall()
        result = [{column: row[i]
                  for i, column in enumerate(result_set[0].keys())}
                  for row in result_set]
        return result


    def get_by_id(self, restaurant_id):
        where_clause = f"WHERE id={restaurant_id}"
        return self.list_restaurants(where_clause)
