from rest_framework.test import APITestCase
from vocations.models import Vocation
from accounts.models import Account
from rest_framework.authtoken.models import Token


class TestCharacterView(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.vocation_one = Vocation.objects.create(
            name="queen",
            intellect_modifier=20,
            strength_modifier=-5,
            agility_modifier=-5,
        )

        cls.admin_account = Account.objects.create_superuser(
            username="neha", password="1234", is_game_master=True
        )
        cls.common_account = Account.objects.create_user(
            username="neha1", password="1234"
        )

        cls.admin_token = Token.objects.create(user=cls.admin_account)

        cls.common_token = Token.objects.create(user=cls.common_account)

    def test_characters_success_creation_admin_user(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.admin_token}")

        res = self.client.post(
            "/api/accounts/characters/",
            data={
                "nickname": "Rainha Mara",
                "vocation": self.vocation_one.id,
            },
        )

        self.assertEqual(res.status_code, 201)
        self.assertIn("id", res.json())

    def test_characters_success_creation_common_user(self):
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Token {self.common_token}"
        )

        res = self.client.post(
            "/api/accounts/characters/",
            data={
                "nickname": "Rainha Mara",
                "vocation": self.vocation_one.id,
            },
        )

        self.assertEqual(res.status_code, 201)
        self.assertIn("id", res.json())


    def test_characters_creation_with_missing_keys(self):
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Token {self.common_token}"
        )

        res = self.client.post(
            "/api/accounts/characters/",
            data={},
        )
        self.assertEqual(res.status_code, 400)
        self.assertIn("nickname", res.json())
        self.assertIn("vocation", res.json())

    def test_characters_creation_without_token(self):
        res = self.client.post(
            "/api/accounts/characters/",
            data={},
        )

        self.assertEqual(res.status_code, 401)
        self.assertIn("detail", res.json())
