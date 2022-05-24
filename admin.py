from django.contrib import admin
from portfolio import models


admin.site.register(models.Portfolio)
admin.site.register(models.PortfolioLink)
admin.site.register(models.Skill)
admin.site.register(models.Project)
admin.site.register(models.Feature)
admin.site.register(models.ProjectLink)


@admin.action(description='Create thumbnails for images')
def make_thumb(modeladmin, request, queryset):
    for x in list(queryset):
        x.make_thumbnail()


@admin.register(models.ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    actions = [make_thumb, ]
    readonly_fields = ('image_tag',)
