from django.contrib import admin
from .models import Users,Role,Priority,Tickets 

admin.site.register(Users)
admin.site.register(Role)
admin.site.register(Priority)
admin.site.register(Tickets)
