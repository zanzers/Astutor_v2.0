from django.contrib import admin
from django.apps  import apps

from .models import Account, AccountType, Register, LoginDetails


admin.site.register(Account)
admin.site.register(AccountType)
admin.site.register(Register)
admin.site.register(LoginDetails)