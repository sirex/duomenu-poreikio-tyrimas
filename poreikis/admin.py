from django.contrib import admin
from mptt.admin import MPTTModelAdmin, TreeRelatedFieldListFilter

from poreikis.models import Request, Project, Dataset, Organization, Category


class RequestDatasetInline(admin.TabularInline):
    model = Request.datasets.through
    raw_id_fields = ('dataset',)


class RequestAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'status', 'created', 'updated')
    list_filter = ('status',)
    raw_id_fields = ('project',)
    inlines = [RequestDatasetInline, TreeRelatedFieldListFilter]
    exclude = ('datasets',)


class ProjectAdmin(admin.ModelAdmin):
    pass


class DatasetAdmin(admin.ModelAdmin):
    pass


class OrganizationAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(MPTTModelAdmin):
    pass


admin.site.register(Request, RequestAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Dataset, DatasetAdmin)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Category, CategoryAdmin)
