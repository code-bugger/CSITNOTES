from django.contrib import admin
from .models import Semester,Subject,Note,Question
# Register your models here.
admin.site.register(Semester)
admin.site.register(Subject)
admin.site.register(Note)
admin.site.register(Question)