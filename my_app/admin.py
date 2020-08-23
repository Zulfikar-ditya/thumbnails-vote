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
        'img',
        'img2',
        'img3',
        'status',
        'user',
    ]


class VoteAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'vote_img_1',
        'vote_img_2',
        'vote_img_3',

    ]

admin.site.register(Pool, PoolAdmin)
admin.site.register(Categories, CatageriesAdmin)
admin.site.register(Vote, VoteAdmin)