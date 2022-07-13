from rest_framework.test import APITestCase
from accounts.models import Account


class TestAccountView(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        ...

    def test_non_admin_account_creation_success(self):
        res = self.client.post(
            "/api/accounts/register/", data={"username": "nehama", "password": "1234"}
        )
        self.assertEqual(res.status_code, 201)
        self.assertIn("id", res.json())
        self.assertIn("classification", res.json())
        self.assertNotIn("password", res.json())

    def test_admin_account_creation_success(self):
        res = self.client.post(
            "/api/accounts/register/",
            data={"username": "nehama", "password": "1234", "is_game_master": "true"},
        )
        self.assertEqual(res.status_code, 201)
        self.assertIn("id", res.json())
        self.assertIn("classification", res.json())
        self.assertNotIn("password", res.json())

    def test_create_account_with_missing_keys(self):
        res = self.client.post("/api/accounts/register/", data={})
        self.assertEqual(res.status_code, 400)
        self.assertIn("username", res.json())
        self.assertIn("password", res.json())

    def test_create_account_with_invalid_classification(self):
        res = self.client.post(
            "/api/accounts/register/",
            data={
                "username": "nehama",
                "password": "1234",
                "is_game_master": "true",
                "classification": "hahaha",
            },
        )
        self.assertEqual(res.status_code, 400)
        self.assertIn("classification", res.json())

    def test_list_all_accounts(self):
        Account.objects.create_user(username="nene", password="1234")
        Account.objects.create_user(username="nene1", password="1234")

        res = self.client.get("/api/accounts/")

        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.json()), 2)

    def test_login_non_admin_user_returns_token(self):
        Account.objects.create_user(username="nene", password="1234")
        res = self.client.post(
            "/api/accounts/login/", data={"username": "nene", "password": "1234"}
        )
        self.assertEqual(res.status_code, 200)
        self.assertIn("token", res.json())

    def test_login_admin_user_returns_token(self):
        Account.objects.create_superuser(username="nene", password="1234")
        res = self.client.post(
            "/api/accounts/login/", data={"username": "nene", "password": "1234"}
        )
        self.assertEqual(res.status_code, 200)
        self.assertIn("token", res.json())

    def test_login_with_invalid_credentials(self):
        Account.objects.create_user(username="nene", password="1234")

        res = self.client.post(
            "/api/accounts/login/", data={"username": "nene", "password": "123"}
        )

        self.assertEqual(res.status_code, 401)
        self.assertIn("message", res.json())
