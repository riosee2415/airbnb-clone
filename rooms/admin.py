from django.contrib import admin
from . import models


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRole)
class ItemAdmin(admin.ModelAdmin):
    """ Item Admin Definition """

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """ Item Admin Definition """

    pass


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """ Photo admin Definition """

    pass
