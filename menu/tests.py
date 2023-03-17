from django.test import TestCase

# Create your tests here.
from menu.models import FoodCategory, Topping, Food


class SmokeAPITests(TestCase):
    """
    If no food exist, empty list is returned.
    """
    def test_server_normal_response_no_food(self):
        response = self.client.get('/api/categories/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, [])


class CRUDAPITests(TestCase):
    """
    Check the food is created, filtered and managed properly.
    """
    def create_data(self):
        choc = Topping.objects.create(name='Шоколад')
        straw = Topping.objects.create(name='Клубника')
        drinks = FoodCategory.objects.create(name='Напитки')
        desserts = FoodCategory.objects.create(name='Десерты')
        toppings = Topping.objects.all()
        cocktail_1 = Food.objects.create(name="Молочный коктейль", is_publish=False, price=100,
                                         category=FoodCategory.objects.get(id=1))
        cocktail_2 = Food.objects.create(name="Кофе", is_publish=True, is_vegan=True, price=50,
                                         category=FoodCategory.objects.get(id=1))
        cheesecake = Food.objects.create(name="Чизкейк", is_publish=True, is_special=True, price=200,
                                         category=FoodCategory.objects.get(id=2))
        cocktail_1.toppings.set(toppings)
        cocktail_2.toppings.set(toppings)
        cheesecake.toppings.set(toppings)

    def test_get_all_cats(self):
        self.create_data()
        expected_data = ["Кофе", "Чизкейк"]
        response = self.client.get('/api/categories/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_data)

    def test_get_special_food(self):
        self.create_data()
        response = self.client.get('/api/categories/?is_special=true')
        expected_data = ["Чизкейк"]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_data)

    def test_get_special_vegan_food(self):
        self.create_data()
        response = self.client.get('/api/categories/?food__is_vegan=true&food__is_special=true')
        expected_data = []
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_data)
