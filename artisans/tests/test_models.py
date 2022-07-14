from django.test import TestCase
from artisans.models import Artisan


class ArtisanModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.name = "Arkkie"

        cls.artisan = Artisan.objects.create(name=cls.name)

    def test_name_max_length(self):
        artisan = Artisan.objects.get(id=self.artisan.id)
        max_length = artisan._meta.get_field("name").max_length
        self.assertEquals(max_length, 50)

    def test_artisan_has_information_fields(self):
        self.assertEqual(self.artisan.name, self.name)

