from django.contrib import admin
from  floors.models import user,person_details,floors,Company_details


# Register your models here.


admin.site.register(user)
admin.site.register(Company_details)
admin.site.register(floors)
admin.site.register(person_details)



class useradmin(admin.ModelAdmin):
    list_filter = []
    list_display = []
    search_fields = []


class flooradmin(admin.ModelAdmin):
    list_filter = []
    list_display = []
    search_fields = []


class personadmin(admin.ModelAdmin):
    list_filter = []
    list_display = []
    search_fields = []

class companyadmin(admin.ModelAdmin):
    list_display = []
    list_filter = []
    search_fields = []



