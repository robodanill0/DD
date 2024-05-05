from django.contrib import admin
from .models import BugReport, FeatureRequest

@admin.action(description='Установить статус "На рассмотрении')
def make_published(modeladmin, request, queryset):
    queryset.update(status='Рассмотрение')

# Inline класс для модели BugReport
class BugReportInline(admin.TabularInline):
    model = BugReport
    extra = 0
    fields = ('title', 'project', 'description', 'status', 'priority', 'task', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    can_delete = True
    show_change_link = True
    
# Inline класс для модели FeatureRequest
class FeatureRequestInline(admin.TabularInline):
    model = FeatureRequest
    extra = 0
    fields = ('title', 'project', 'description', 'status', 'priority', 'task', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    can_delete = True
    show_change_link = True
    
# Класс администратора для модели BugReport
@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    actions = [make_published]
    list_display = ('title', 'project', 'task', 'status', 'created_at', 'updated_at', 'priority')
    list_filter = ('status', 'project', 'task')
    search_fields = ('title', 'description')
    list_editable = ('status', 'priority', 'task')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('title', 'project', 'description', 'status', 'priority', 'task')
        }),
        ('Advanced options', {
            'fields': ('created_at', 'updated_at'),
        })
        )
    
# Класс администратора для модели FeatureRequest
@admin.register(FeatureRequest)
class FeatureRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'status', 'task', 'created_at', 'updated_at', 'priority')
    list_filter = ('status', 'project', 'task')
    search_fields = ('title', 'description')
    list_editable = ('status', 'priority', 'task')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('title', 'project', 'description', 'status', 'priority', 'task')
        }),
        ('Advanced options', {
            'fields': ('created_at', 'updated_at'),
        })
        )