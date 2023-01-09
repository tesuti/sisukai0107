from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Dweet,Profile,Account,Comment

class ProfileInline(admin.StackedInline):
    model = Profile


# 追加するときUserNameしか表示しない
class UserAdmin(admin.ModelAdmin):
    model = User
    fields =["username"]
    inlines = [ProfileInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)

admin.site.register(Profile)

admin.site.register(Dweet)

admin.site.register(Account)
admin.site.register(Comment)