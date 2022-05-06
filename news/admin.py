from django.contrib import admin
from news.models import Broadcast, News, Collection


class NewsAdmin(admin.ModelAdmin):
    exclude = ('image_thumb240', 'image_thumb480', 'image_thumb720')
    search_fields = ['name', 'text']
    list_filter = ['active', ]
    list_display = ['name', 'text', 'active']


class BroadcastAdmin(admin.ModelAdmin):
    search_fields = ['username', 'phone_number']
    list_display = ['username', 'phone_number']


class CollectionAdmin(admin.ModelAdmin):
    search_fields = ['name', ]
    list_display = ['name', 'active']
    list_filter = ['active', ]


admin.site.register(News, NewsAdmin)
admin.site.register(Broadcast, BroadcastAdmin)
admin.site.register(Collection, CollectionAdmin)
