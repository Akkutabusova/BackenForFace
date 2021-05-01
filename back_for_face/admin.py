from django.contrib import admin
from .models import User
from .models import QR,Door,Inside,Manager

admin.site.register(User)
admin.site.register(QR)
admin.site.register(Door)
admin.site.register(Inside)
admin.site.register(Manager)