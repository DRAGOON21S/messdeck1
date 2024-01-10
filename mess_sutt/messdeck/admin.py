from django.contrib import admin
from .models import Date, breakfast,lunch,dinner,profile,Feedback,attend

admin.site.register(Date)
admin.site.register(breakfast)
admin.site.register(lunch)
admin.site.register(dinner)
admin.site.register(profile)
admin.site.register(Feedback)
admin.site.register(attend)