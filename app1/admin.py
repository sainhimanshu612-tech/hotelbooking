from django.contrib import admin
from app1.models import Payment,Review,rooms,Facility,Image
# Register your models here.

admin.site.register(Payment)
admin.site.register(Review)
admin.site.register(rooms)
admin.site.register(Facility)
admin.site.register(Image)