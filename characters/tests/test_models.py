from django.test import TestCase
from accounts.models import Account
from vocations.models import Vocation
from characters.models import Character


class CharacterModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.username = "Teste"
        cls.password = "1234"
        cls.nickname = "Eragon"

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
            nickname=cls.nickname,
            vocation=cls.vocation.id,
            account=cls.account
        )

    def test_username_basic(self):
        character = Character.objects.get(id=1)
        max_length = character._meta.get_field("nickname").max_length
        unique = character._meta.get_field("nickname").unique
        self.assertEquals(max_length, 50)
        self.assertEquals(unique, True)

    def test_character_creation_full(self):

        character = Character.objects.get(id=1)

        testModel = {
            character.nickname,
            character.level,
            character.experience,
            character.gold,
            character.health_points,
            character.strength,
            character.intellect,
            character.agility,
        }

        clsModel = {
            self.nickname,
            self.level,
            self.experience,
            self.gold,
            self.health_points,
            self.strength,
            self.intellect,
            self.agility,
        }

        self.assertEquals(testModel, clsModel)
