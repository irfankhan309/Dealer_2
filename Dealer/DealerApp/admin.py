from django.contrib import admin
from DealerApp.models import PostEnquiry
# Register your models here.

class PostEnquiryAdmin(admin.ModelAdmin):
    list_display=['Name','Vehicle','BIKE_Model','Color','Contact_Number']

admin.site.register(PostEnquiry,PostEnquiryAdmin)
