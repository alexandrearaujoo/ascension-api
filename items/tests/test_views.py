from rest_framework.test import APITestCase
from artisans.models import Artisan


class TestItemsView(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:

        cls.createAccount = {
            "username": "user",
            "password": "password",
            "is_game_master": True,
        }

    def setUp(self):

        self.client.post("/api/accounts/register/", self.createAccount, format="json")

        login_data = {
            "username": self.createAccount["username"],
            "password": self.createAccount["password"],
        }

        response = self.client.post("/api/accounts/login/", login_data, format="json")

        self.client.credentials(HTTP_AUTHORIZATION=f'Token {response.data["token"]}')

        self.artisan = self.client.post("/api/artisans/", data={"name": "bryan"})

        self.artisan_id = self.artisan.json()["id"]

        self.artisanItem = self.client.post(
            f"/api/artisans/{self.artisan_id}/items/",
            data={
                "name": "MMS Shield",
                "price": 30,
                "type": "SH",
                "level_required": 5,
            },
        )

        self.item_id = self.artisanItem.json()["id"]

    def test_item_update(self):

        res = self.client.patch(
            f"/api/items/{self.item_id}/",
            data={
                "name": "Sword",
            },
        )

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json()["name"], "Sword")

    def test_item_list(self):
        res = self.client.get(f"/api/items/{self.item_id}/")
        self.assertEqual(res.status_code, 200)
