from typing import Any
from django.contrib import admin
from django.db import models
from django.http import HttpRequest
from django.http.response import HttpResponse
from .models import  Contacts, Logo,Slider,Photos,Projects
from .forms import  BinaryFileInput, LogoForm, SliderForm, ContactForm, PhotoForm
import base64
from django.utils.html import format_html
# Register your models here.


class LogoAdmin(admin.ModelAdmin):
    form = LogoForm
    def logoF(self, obj):
       base64Encoded =  str(base64.b64encode(obj.logo)).split("b'")[1].split("'")[0] 
       return  format_html('<img src="data:;base64,{}" width="200"   height="200" alt="">'.format(base64Encoded))
       
    list_display =['logo_title', 'logoF']
 
admin.site.register(Logo, LogoAdmin)

class SliderAdmin(admin.ModelAdmin):
    form = SliderForm
    def slideF(self, obj):
       base64Encoded =  str(base64.b64encode(obj.slide)).split("b'")[1].split("'")[0]
       return  format_html('<img src="data:;base64,{}" width="200"   height="200" alt="">'.format(base64Encoded))
       
    list_display =['slideF']
admin.site.register(Slider,SliderAdmin)

class ContactsAdmin(admin.ModelAdmin):
    form  = ContactForm
   
    def contactF(self, obj):
       base64Encoded =  str(base64.b64encode(obj.contact_logo)).split("b'")[1].split("'")[0]
       return  format_html('<img src="data:image/*;base64,{}"   height="200" alt="">'.format(base64Encoded))

    list_display = ['contact_title', 'contact_link','contactF']
admin.site.register(Contacts,ContactsAdmin)


class PhotoAdmin(admin.ModelAdmin):
    form = PhotoForm
    def photoF(self, obj):
       base64Encoded =  str(base64.b64encode(obj.photo)).split("b'")[1].split("'")[0]
       return  format_html('<img src="data:image/*;base64,{}"   height="200" alt="">'.format(base64Encoded))

    list_display = ['photo_name','project','photoF']
admin.site.register(Photos,PhotoAdmin)


class PhotoInline(admin.TabularInline):
    model = Photos  
   
    extra = 0
class ProjectsAdmin(admin.ModelAdmin):
    model = Projects
#     inlines = [PhotoInline]
#     formfield_overrides = {
#         models.BinaryField: {'widget': BinaryFileInput()}
       
#     }
#     def get_inline_instances(self, request, obj=None):
#         return [inline(self.model, self.admin_site) for inline in self.inlines]
#     list_display = ['name','Description']
#     def get_readonly_fields(self, request, obj=None):
#        if obj:
#            return ['name']
#        return self.readonly_fields
admin.site.register(Projects, ProjectsAdmin)


