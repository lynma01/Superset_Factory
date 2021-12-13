import datetime
import factory
import random
import objects


class AccountFactory(factory.Factory):
    class Meta:
        model = objects.Account

    username = factory.Sequence(lambda n: 'john%s' % n)
    email = factory.LazyAttribute(lambda o: '%s@example.org' % o.username)
    date_joined = factory.LazyFunction(datetime.datetime.now)


class ProfileFactory(factory.Factory):
    class Meta:
        model = objects.Profile

    account = factory.SubFactory(AccountFactory)
    gender = factory.Iterator([objects.Profile.GENDER_MALE, objects.Profile.GENDER_FEMALE])
    firstname = "John"
    lastname = 'Doe'


class FemaleProfileFactory(ProfileFactory):
    gender = objects.Profile.GENDER_FEMALE
    firstname = 'Jane'
    account__username = factory.Sequence(lambda n: 'jane%s' % n)
