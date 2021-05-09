from django.contrib import admin
from .models import UserModel, VerifyCode


@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'name',
        'student_id'
    )

    list_display_links = (
        'email',
        'name',
        'student_id'
    )


admin.site.register(VerifyCode)
