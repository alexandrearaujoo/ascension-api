from django.test import TestCase
from missions.models import Missions
from accounts.models import Account


class missionModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.description = "Must create a software"
        cls.name = "dev"
        cls.experience = 3
        cls.level_required = 6
        cls.gold = 10

        cls.account = Account.objects.create(username="Arkkie", password="abcd")

        cls.mission = Missions.objects.create(
            description=cls.description,
            name=cls.name,
            experience=cls.experience,
            level_required=cls.level_required,
            gold=cls.gold,
            created_by=cls.account,
        )

    def test_name_max_length(self):
        mission = Missions.objects.get(id=1)
        max_length = mission._meta.get_field("name").max_length
        self.assertEquals(max_length, 50)

    def test_patron_has_information_fields(self):
        self.assertEqual(self.mission.description, self.description)
        self.assertEqual(self.mission.name, self.name)
        self.assertEqual(self.mission.experience, self.experience)
        self.assertEqual(self.mission.level_required, self.level_required)
        self.assertEqual(self.mission.gold, self.gold)
