from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from artisans.models import Artisan


class TestViews(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.artisans = [
            Artisan.objects.create(name=f"Shield Maker {index}")
            for index in range(1, 4)
        ]

        cls.account = {
            "username": "user",
            "password": "password",
            "is_game_master": True,
        }

        cls.item = {
            "name": "MMS Shield",
            "price": 30,
            "type": "SH",
            "level_required": 5,
        }

    def setUp(self) -> None:
        self.client.post("/api/accounts/register/", self.account, format="json")

        login_data = {
            "username": self.account["username"],
            "password": self.account["password"],
        }

        response = self.client.post("/api/accounts/login/", login_data, format="json")

        self.client.credentials(HTTP_AUTHORIZATION=f'Token {response.data["token"]}')

    def test_list_artisans(self):

        response = self.client.get("/api/artisans/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.data[0]["name"], self.artisans[0].name)
        self.assertEqual(response.data[1]["name"], self.artisans[1].name)
        self.assertEqual(response.data[2]["name"], self.artisans[2].name)

    def test_list_one_artisan(self):
        response = self.client.get(f"/api/artisans/{self.artisans[0].id}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["name"], self.artisans[0].name)

    def test_create_artisan(self):

        response = self.client.post(
            "/api/artisans/",
            {"name": "Shield Maker 4"},
            format="json",
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["name"], "Shield Maker 4")

    def test_create_item(self):
        response = self.client.post(
            f"/api/artisans/{self.artisans[0].id}/items/",
            self.item,
            format="json",
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["name"], self.item["name"])
        self.assertEqual(response.data["price"], self.item["price"])
        self.assertEqual(response.data["type"], self.item["type"])
        self.assertEqual(response.data["level_required"], self.item["level_required"])

    def test_update_artisan(self):
        response = self.client.patch(
            f"/api/artisans/{self.artisans[0].id}/",
            {"name": "Sword Maker"},
            format="json",
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["name"], "Sword Maker")

    def test_delete_artisan(self):

        response = self.client.delete(f"/api/artisans/{self.artisans[0].id}/")

        self.assertEqual(response.status_code, 204)
