import unittest
from app import factories
from app import models


class MyTestCase(unittest.TestCase):

    def test_send_mail(self):
        account = factories.AccountFactory()
        email = business_logic.prepare_email(account, subject='Foo', text='Bar')

        self.assertEqual(email.to, account.email)

    def test_get_profile_stats(self):
        profiles = []

        profiles.extend(factories.ProfileFactory.create_batch(4))
        profiles.extend(factories.FemaleProfileFactory.create_batch(2))
        profiles.extend(factories.ProfileFactory.create_batch(2, planet="Tatooine"))

        stats = business_logic.profile_stats(profiles)
        self.assertEqual({'Earth': 6, 'Mars': 2}, stats.planets)
        self.assertLess(stats.genders[models.Profile.GENDER_FEMALE], 2)