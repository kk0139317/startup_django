from django.contrib import admin
from home.models import ContactMessage, Profile, SubmitForm, NewSubmitForm

# Register your models here.


admin.site.register(ContactMessage)
admin.site.register(Profile)
admin.site.register(NewSubmitForm)
admin.site.register(SubmitForm)