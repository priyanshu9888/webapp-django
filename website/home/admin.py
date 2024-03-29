from django.contrib import admin
from home.models import Apointment 
from home.models import Contact
from home.models import Tdata
from import_export.admin import ImportExportModelAdmin
from .models import *


# Register  Apointment  models here.

class ApointmentAdmin( ImportExportModelAdmin ,admin.ModelAdmin):
    list_display=('name', 'phone','email','option','desc')
admin.site.register(Apointment , ApointmentAdmin)



# Register Contact Model Here.
class ContactAdmin( ImportExportModelAdmin, admin.ModelAdmin):
    list_display=('name','email','phone','desc', )
admin.site.register(Contact , ContactAdmin)


#Register Tdata Model Here.
class TdataAdmin(ImportExportModelAdmin ,admin.ModelAdmin ):
    list_display=('fullname','alias','father','placeofbirth','dateofbirth',
     'gender','martial','nationality','language','contactnum','contactnum2','adhar',
     'Linkno','Occupation','nameofcompany','ownername','ownerno','socityname',
     'address','namestay','relationship','numb','address2','address3','state',
     'pincode','police','period','presentsameperma','peraddress','pervillcity','state2','pincode2',
     'police2','period2','image1','image2','image3','image4',)
admin.site.register( Tdata, TdataAdmin)


#Register Profile Model Here.
@admin.register(Profile)
class ProfileAdmin( ImportExportModelAdmin , admin.ModelAdmin):
    list_display = ['user','phone_number','email_verified','uuid']
