import datetime
import factory
import random
import models


class AccountFactory(factory.Factory):
    class Meta:
        model = models.Account

    username = factory.Sequence(lambda n: 'john%s' % n)
    email = factory.LazyAttribute(lambda o: '%s@example.org' % o.username)
    date_joined = factory.LazyFunction(datetime.datetime.now)


class ProfileFactory(factory.Factory):
    class Meta:
        model = models.Profile

    account = factory.SubFactory(AccountFactory)
    gender = factory.Iterator([models.Profile.GENDER_MALE, models.Profile.GENDER_FEMALE])
    firstname = factory.Faker('first_name')
    lastname = factory.Faker('last_name')


class FemaleProfileFactory(ProfileFactory):
    gender = models.Profile.GENDER_FEMALE
    firstname = factory.Faker('first_name_female')
    account__username = factory.Sequence(lambda n: 'jane%s' % n)
