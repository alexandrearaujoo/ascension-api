from django.test import TestCase
from accounts.models import Account
from vocations.models import Vocation
from characters.models import Character


class AccountModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):

        cls.username = "Eragon"
        cls.password = "12345"
        cls.level = 1
        cls.experience = 10
        cls.gold = 100
        cls.health_points = 10
        cls.strength = 20
        cls.intellect = 5
        cls.agility = 10

        cls.name = "Craftsman"
        cls.intellect_modifier = 10.00
        cls.strength_modifier = 10.00
        cls.agility_modifier = 10.00

        cls.account = Account.objects.create(
            username=cls.username, password=cls.password
        )
        cls.vocation = Vocation.objects.create(
            name=cls.name,
            intellect_modifier=cls.intellect_modifier,
            strength_modifier=cls.strength_modifier,
            agility_modifier=cls.agility_modifier,
        )
        cls.characters = Character.objects.create(
            username=cls.username,
            password=cls.password,
            vocation=cls.vocation,
            account=cls.account,
            level=cls.level,
            experience=cls.experience,
            gold=cls.gold,
            health_points=cls.health_points,
            strength=cls.strength,
            intellect=cls.intellect,
            agility=cls.agility,
        )

    def test_username_basic(self):
        character = Character.objects.get(id=1)
        max_length = character._meta.get_field("username").max_length
        unique = character._meta.get_field("username").unique
        self.assertEquals(max_length, 50)
        self.assertEquals(unique, True)

    def test_password_basic(self):
        character = Character.objects.get(id=1)
        max_length = character._meta.get_field("password").max_length
        self.assertEquals(max_length, 255)

    def test_character_creation_full(self):

        character = Character.objects.get(id=1)

        testModel = {
            character.username,
            character.password,
            character.level,
            character.experience,
            character.gold,
            character.health_points,
            character.strength,
            character.intellect,
            character.agility,
        }

        clsModel = {
            self.username,
            self.password,
            self.level,
            self.experience,
            self.gold,
            self.health_points,
            self.strength,
            self.intellect,
            self.agility,
        }

        self.assertEquals(testModel, clsModel)
