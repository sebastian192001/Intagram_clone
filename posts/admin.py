# Django
from django.contrib import admin
# Posts
from posts.models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post admin"""
    list_display = ('id', 'title', 'photo', 'user')
    list_display_links = ('id', 'title')
    search_fields = (
        'title',
        'user__email',
        'user__first_name',
        'user__last_name',
        'profile__phone_number')
    list_filter = (
        'title',
        'create',
        'modified',
        'user__is_active',
        'user__is_staff')

    fieldsets = (
        ('Post Info', {
            'fields': (
                ('title', 'photo'),
            ),
        }),
        ('User Info', {
            'fields': (
                ('user', 'profile'),
            ),
        }),
        ('Metadata', {
            'fields': (
                ("create", "modified"),
            ),
        })
    )

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['user', 'profile', "create", "modified"]
        else:
            return ["create", "modified"] 