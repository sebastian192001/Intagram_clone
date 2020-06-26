
#Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

#Models

from users.models import Profile

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    
    list_display = ("pk","user","phone_number","website","picture")

    list_display_links= ("pk","user",)

    list_editable= ("phone_number","website","picture")

    search_fields = (
        "user__email",
        "user__first_name",
        "user__last_name",
        "user__username",
        "phone_number"
    )

    list_filter=(
        "user__is_active",
        "user__is_staff",
        "create",
        "modified",
    )

    fieldsets = (
        ("Profile", {
            'fields': (('user', 'picture'),),
        }),
        ("Extra info", {
            "fields": (
                ("website","phone_number"),
                ("biography"),
            )
        }),

        ("Metadata",{
            "fields":(("create", "modified"),),
        }),
    )

    readonly_fields=("create","modified",)

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete=False
    verbose_name_plural="profiles"

class UserAdmin(BaseUserAdmin):
    inlines=(ProfileInline,)

    list_display=(
        "username",
        "email",
        "first_name",
        "last_name",
        "is_active",
        "is_staff",
    )


admin.site.unregister(User)

admin.site.register(User,UserAdmin)