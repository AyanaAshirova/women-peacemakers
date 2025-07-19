from django.contrib import admin
from django.utils.html import format_html
from .models import *

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'image_tag', 'views')  # Отобразит фото в списке
    readonly_fields = ('image_tag',)  # Чтобы изображение было видно в форме
    fields = ('title', 'image', 'image_tag', 'content')

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 100px;"/>', obj.image.url)
        return "-"
    image_tag.short_description = "Image"

admin.site.register(ContactInfo)
admin.site.register(SocialNetwork)
admin.site.register(News, NewsAdmin)
admin.site.register(PodcastChannel)
admin.site.register(PodcastRelease)
admin.site.register(MainSlider)
