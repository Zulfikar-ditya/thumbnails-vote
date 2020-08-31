from django.contrib import admin

from .models import Categories, Pool

# Register your models here.
class CatageriesAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
    ]


class PoolAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'date_add',
        'title',
        'status',
        'user',
        'img_1',
        'img_2',
    ]


admin.site.register(Pool, PoolAdmin)
admin.site.register(Categories, CatageriesAdmin)