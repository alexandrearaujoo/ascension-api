from django.test import TestCase
from missions.models import Missions
from accounts.models import Account


class missionModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):

        cls.description = "Kill 10 monsters"
        cls.name = "Kill monsters"
        cls.experience = 10
        cls.level_required = 1
        cls.gold = 100

        cls.account = Account.objects.create(username="Eragon", password="1234")

        cls.mission = Missions.objects.create(
            description=cls.description,
            name=cls.name,
            experience=cls.experience,
            level_required=cls.level_required,
            gold=cls.gold,
            created_by=cls.account,
        )

  
