# _*_ encoding:utf-8 _*_
from django.contrib import admin

# Register your models here.


from .models import address_info, weights


class ManagePoint(admin.ModelAdmin):
    list_display = ('index', 'data', 'longitude', 'latitude')  # list
    search_fields = ('data',)
    list_filter = ['data']
    fields = ('index', 'data', 'longitude', 'latitude')


class ManageWeight(admin.ModelAdmin):
    list_display = ('index1', 'index2', 'weight', 'state')  # list
    search_fields = ('index1', 'index2')
    list_filter = ['state']
    fields = ('index1', 'index2', 'weight', 'state')


admin.site.register(address_info, ManagePoint)
admin.site.register(weights, ManageWeight)
