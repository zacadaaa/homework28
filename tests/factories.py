
import factory.django

from users.models import User
from ads.models import Ads


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("name")
    password = "123test"


class AdFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ads

    name = "Temp-name for test"
    price = 100
    description = ""
    author = factory.SubFactory(UserFactory)