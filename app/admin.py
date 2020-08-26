from django.contrib import admin
from .models import FavRecord, ShelfRecord, WishRecord

admin.site.register(FavRecord)
admin.site.register(ShelfRecord)
admin.site.register(WishRecord)