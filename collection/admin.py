from django.contrib import admin
from .models import * 

class PersonAdmin(admin.ModelAdmin): 
    list_display = ['first_name', 'last_name', 'gender', 'dob', 'contact', 'active']
    # list_editable = ['last_name', 'gender', 'dob', 'contact', 'active']
    list_display_links = ['first_name', 'last_name', 'gender', 'dob', 'contact', 'active']
    # list_per_page = 1
    search_fields =['first_name', 'last_name', 'gender', 'dob', 'contact', 'active']


# admin.site.register(Person, PersonAdmin)
# admin.site.register(Course)

# class ScoreAdmin(admin.ModelAdmin): 
#     autocomplete_fields = ['person']
# admin.site.register(Score, ScoreAdmin)

# # Register your models here.
