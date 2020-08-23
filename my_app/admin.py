from django.contrib import admin

from .models import Vote, Categories, Pool

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
    ]


class VoteAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'image',
        'vote',

    ]

admin.site.register(Pool, PoolAdmin)
admin.site.register(Categories, CatageriesAdmin)
admin.site.register(Vote, VoteAdmin)