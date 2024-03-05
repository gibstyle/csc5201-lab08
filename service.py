from models import RestaurantModel


class RestaurantService:
    def __init__(self):
        self.model = RestaurantModel()


    def create(self, params):
        return self.model.create(params)


    def update(self, restaurant_id, params):
        return self.model.update(restaurant_id, params)
    

    def delete(self, restaurant_id):
        return self.model.delete(restaurant_id)


    def list(self):
        return self.model.list_restaurants()


    def get_by_id(self, restaurant_id):
        return self.model.get_by_id(restaurant_id)
