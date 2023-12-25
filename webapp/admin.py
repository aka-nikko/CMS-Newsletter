from django.contrib import admin

# Register your models here.
from .models import Newsletter, Submission, Quarter, Topic

admin.site.register(Submission)
admin.site.register(Newsletter)
admin.site.register(Quarter)
admin.site.register(Topic)