from django.test import TestCase
from restaurant.models import MenuItem


class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title="pasta", price=2.30 , inventory=3)
        itemstr = item.get_item()

        self.assertEqual(itemstr, "pasta : 2.30")

