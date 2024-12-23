from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(TransportAdmin)
admin.site.register(Car)
admin.site.register(Task)
admin.site.register(Payment)

#@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'plate_number', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'plate_number')