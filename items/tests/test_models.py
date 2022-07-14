from django.test import TestCase
from items.models import Item


class itemModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.name = "Arkkie"
        cls.type = "Sword"
        cls.price = 22

        cls.item = Item.objects.create(name=cls.name, type=cls.type, price=cls.price)

    def test_name_max_length(self):
        item = Item.objects.get(id=self.item.id)
        max_length = item._meta.get_field("name").max_length
        self.assertEquals(max_length, 50)

    def test_type_max_length(self):
        item = Item.objects.get(id=self.item.id)
        max_length = item._meta.get_field("type").max_length
        self.assertEquals(max_length, 50)

    def test_item_has_information_fields(self):
        self.assertEqual(self.item.name, self.name)
        self.assertEqual(self.item.type, self.type)
        self.assertEqual(self.item.price, self.price)
        self.assertEqual(self.item.level_required, 0)
