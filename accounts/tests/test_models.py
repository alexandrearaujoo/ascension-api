from django.test import TestCase
from accounts.models import Account

class AccountModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.username = "Arkkie"
        cls.classification = "angel"
        cls.is_game_master = False

        cls.account = Account.objects.create(
            username=cls.username, 
            password='abcd'
        ) 

    def test_username_max_length(self):
        account = Account.objects.get(id=1)
        max_length = account._meta.get_field('username').max_length
        self.assertEquals(max_length, 50)

    def test_classification_max_length(self):
        account = Account.objects.get(id=1)
        max_length = account._meta.get_field('classification').max_length
        self.assertEquals(max_length, 50)
    
    def test_patron_has_information_fields(self):              
        self.assertEqual(self.account.username, self.username)
        self.assertEqual(self.account.classification, self.classification)
        self.assertFalse(self.account.is_game_master)