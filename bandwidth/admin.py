from django.contrib import admin
from .models import *


class authorModel(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__","details"]
    class Meta:
        Model=author

admin.site.register(author, authorModel)
admin.site.register(category)



class articleModel(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__","add_date"]
    list_filter = ["add_date", "category"]
    class Meta:
        Model=article

admin.site.register(article, articleModel)
admin.site.register(upgrade)
