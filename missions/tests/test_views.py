from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from missions.models import Missions
from accounts.models import Account
from vocations.models import Vocation
from characters.models import Character


class TestMissionsView(APITestCase):
    @classmethod
    def setUpTestData(cls):

        cls.createAccount = {
            "username": "user",
            "password": "password",
            "is_game_master": True,
        }

        cls.account = Account.objects.create(username="bryan", password="1234")

        cls.description = "Kill 10 monsters"
        cls.name = "Kill monsters"
        cls.experience = 10
        cls.level_required = 1
        cls.gold = 100
        cls.created_by = cls.account

        Missions.objects.create(
            description=cls.description,
            name=cls.name,
            experience=cls.experience,
            level_required=cls.level_required,
            gold=cls.gold,
            created_by=cls.created_by,
        )

        cls.nickname = "bryan"
        cls.password = "1234"
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

        cls.vocation = Vocation.objects.create(
            name=cls.name,
            intellect_modifier=cls.intellect_modifier,
            strength_modifier=cls.strength_modifier,
            agility_modifier=cls.agility_modifier,
        )

        Character.objects.create(
            nickname=cls.nickname,
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

    def setUp(self):

        self.client.post(
            "/api/accounts/register/", self.createAccount, format="json"
        )

        login_data = {
            "username": self.createAccount["username"],
            "password": self.createAccount["password"],
        }

        response = self.client.post(
            "/api/accounts/login/", login_data, format="json"
        )

        self.client.credentials(
            HTTP_AUTHORIZATION=f'Token {response.data["token"]}'
        )

    def test_mission_creation(self):

        res = self.client.post(
            "/api/missions/",
            data={
                "description": self.description,
                "name": self.name,
                "experience": self.experience,
                "level_required": self.level_required,
                "gold": self.gold,
                "created_by": self.account,
            },
        )

        self.assertEqual(res.status_code, 201)

    def test_updating_mission(self):

        newDescription = "Kill 5 monsters"

        res = self.client.patch(
            "/api/missions/2/",
            data={
                "description": newDescription,
            },
        )

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json()["description"], newDescription)

    def test_listing_a_characters_missions(self):
        res = self.client.get("/api/missions/patron/1/")

        self.assertEqual(res.status_code, 200)
