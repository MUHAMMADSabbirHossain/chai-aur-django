from django.contrib import admin
from .models import Tweet
from django.utils.html import format_html

# Register your models here.

# admin.site.register(Tweet)
@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = (
        'user_username',
        'short_text',
        'image_preview',
        'created_at',
        'updated_at',
    )
    search_fields = ('text', 'user__username')
    list_filter = ('created_at', 'updated_at', 'user')

    def user_username(self, obj):
        return obj.user.username
    user_username.short_description = 'Username'
    user_username.admin_order_field = 'user__username'

    def short_text(self, obj):
        if not obj.text:
            return ''
        return obj.text if len(obj.text) <= 50 else obj.text[:47] + '...'
    short_text.short_description = 'tweet'
    short_text.admin_order_field = 'text'

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height:50px; max-width:100px; border-radius:5px" />',
                obj.image.url
            )
        return "-"
    image_preview.short_description = 'Image'
