class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = 0
    def describe_restaurant(self):
        print(f"Название ресторана: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")
        print(f"Рейтинг: {self.rating}")
    def open_restaurant(self):
        print("Ресторан открыт")
    def update_rating(self, new_rating):
        self.rating = new_rating
restaurant1 = Restaurant("Теремок", "русская")
restaurant2 = Restaurant("Токио-city", "японская")
restaurant3 = Restaurant("Бао По", "тайская")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

restaurant1.update_rating(4.1)
restaurant2.update_rating(4.4)
restaurant3.update_rating(4.8)

print("\nПосле обновления рейтингов:")
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()