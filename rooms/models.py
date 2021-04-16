from django.db import models
from core import models as core_models
from django_countries.fields import CountryField


class AbstractItem(core_models.TimeStampedModel):
    """ AbstarctItem Definition """

    name = models.CharField(max_length=80)

    class Meata:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):
    """ RoomType Object Model Definition """

    class Meta:
        verbose_name_plural = "Room Types"
        ordering = ["name"]


class Amenity(AbstractItem):
    """ Amenity Object Model Definition """

    class Meta:
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):
    """ Facility Object Model Definition """

    class Meta:
        verbose_name_plural = "Facilities"


class HouseRole(AbstractItem):
    """ HouseRole Object Model Definition """

    class Meta:
        verbose_name_plural = "House Rules"


class Photo(core_models.TimeStampedModel):
    """ Photo Model Difinition """

    caption = models.CharField(max_length=80)
    file = models.ImageField()
    room = models.ForeignKey("Room", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


class Room(core_models.TimeStampedModel):

    """ Room Model Difinition """

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)

    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()

    check_in = models.TimeField()
    check_out = models.TimeField()

    instant_book = models.BooleanField(default=False)

    host = models.ForeignKey("users.User", on_delete=models.CASCADE)

    room_type = models.ForeignKey("RoomType", on_delete=models.SET_NULL, null=True)
    amenities = models.ManyToManyField("Amenity", blank=True)
    facilities = models.ManyToManyField("Facility", blank=True)
    house_roles = models.ManyToManyField("HouseRole", blank=True)

    def __str__(self):
        return self.name
