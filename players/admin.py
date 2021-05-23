from django.contrib import admin
from .models import Players, Fixtures, Transfernews, Profile, Comment

class ProductAdmin(admin.ModelAdmin):
	list_display = ('name', 'position')


class FixturesAdmin(admin.ModelAdmin):
	list_display = ('home_team', 'away_team')


class TransfernewsAdmin(admin.ModelAdmin):
	list_display = ('player_name', 'player_description')


admin.site.register(Players, ProductAdmin)
admin.site.register(Fixtures, FixturesAdmin)
admin.site.register(Transfernews, TransfernewsAdmin)
admin.site.register(Profile)
admin.site.register(Comment)