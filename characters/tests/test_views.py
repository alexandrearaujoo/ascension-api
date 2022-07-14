from rest_framework.test import APITestCase
from vocations.models import Vocation
from accounts.models import Account


class TestCharacterView(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.vocation_one = Vocation.objects.create(
            username="queen",
            intellect_modifier=20,
            strength_modifier=-5,
            agility_modifier=-5,
        )

        cls.admin_account = Account.objects.create_superuser(
            username="neha", passsword="1234", is_game_master="true"
        )
        cls.common_account = Account.objects.create_user(
            username="neha1", passsword="1234"
        )

        # cls.admin_token =
        # cls.common_token =

    def test_characters(self):
        ...
