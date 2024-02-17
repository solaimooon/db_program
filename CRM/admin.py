from django.contrib import admin
from .models import *
from django.contrib.admin import AdminSite
from  django.contrib.auth.models import Group





class Adress_admin (admin.TabularInline):
    model = Adress
    list_display =["city","number_of_region","street","detail_adress"]
    list_filter=['number_of_region']
    extra = 0


class Phone_admin(admin.TabularInline):
    model = Phone
    list_display =['number','identity']
    extra = 0


class User_admin(admin.ModelAdmin):
    list_display = ['نام','age','join_at','marital_status','level_of_life','marital_status']
    inlines = [Adress_admin,Phone_admin]
    list_filter = ['age','level_of_life']
    search_fields = ['first_name','user_name','last_name']






#admin.site.register(marital_status)
#admin.site.register(level_of_life)
#admin.site.register(membership_type)
admin.site.unregister(Group)
admin.site.register(Users,User_admin)
#admin.site.register(Adress)
#admin.site.register(Phone)
#admin.site.register(Point)


# Register your models here.
