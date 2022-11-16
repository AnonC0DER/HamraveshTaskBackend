from django.contrib import admin
from datetime import datetime
from manager.models import App, Container

@admin.register(App)
class AppAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'created_at', 'get_human_friendly_last_run')
    search_fields = ('name', 'user__username')

    @admin.display(description='Last run')
    def get_human_friendly_last_run(self, obj):
        '''Returns human friendly last_run'''
        if obj.last_run:
            return obj.last_run.strftime('%I:%M:%S%p %d%b%Y')
        
        return None


@admin.register(Container)
class ContainerAdmin(admin.ModelAdmin):
    list_display = ('name', 'app', 'get_human_friendly_created_at', 'status')
    search_fields = ('name', 'status')
    list_filter = ('status',)

    @admin.display(description='Created at')
    def get_human_friendly_created_at(self, obj):
        '''Returns human friendly created_at'''
        return obj.created_at.strftime('%I:%M:%S%p %d%b%Y')