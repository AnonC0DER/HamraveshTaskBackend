from django.contrib import admin
from manager.models import App, Container

@admin.register(App)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'created_at')
    search_fields = ('name', 'user__username')


@admin.register(Container)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'app', 'created_at', 'last_run')
    search_fields = ('name', 'status')
    list_filter = ('status',)
