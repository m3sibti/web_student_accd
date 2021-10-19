from django.contrib import admin
from std_acc_app.models import User, Advertisement

# Register your models here.
admin.site.register([User, Advertisement])
