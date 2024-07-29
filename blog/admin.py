from django.contrib import admin
from blog.models import Blog, ContactUs
from django.contrib.auth.models import User

# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id','title','author']

@admin.register(ContactUs)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id','username','title','created_at']