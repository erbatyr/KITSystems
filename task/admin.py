from django.contrib import admin
from .models import Status, Task, StatusEditing, Reminder

# Register your models here.
admin.site.register(Task)
admin.site.register(Status)
admin.site.register(StatusEditing)
admin.site.register(Reminder)
