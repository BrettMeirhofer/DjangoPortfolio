from django.contrib import admin
from portfolio import models


admin.site.register(models.Project)


@admin.action(description='Create thumbnails for images')
def make_thumb(modeladmin, request, queryset):
    for x in list(queryset):
        x.make_thumbnail()


@admin.register(models.ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_filter = ["project"]
    list_display = ["image_name", "project"]
    actions = [make_thumb, ]
    readonly_fields = ('image_tag',)


@admin.register(models.Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_filter = ["person_name"]
    list_display = ["person_name"]


@admin.register(models.Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_filter = ["project", "current"]
    list_display = ["feature_name", "current", "project"]


@admin.register(models.Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ["skill_name"]


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["category_name"]


@admin.register(models.ProjectLink)
class ProjectLinkAdmin(admin.ModelAdmin):
    list_filter = ["project"]
    list_display = ["link_name", "project"]


@admin.register(models.PortfolioLink)
class PortfolioLinkAdmin(admin.ModelAdmin):
    list_filter = ["portfolio"]
    list_display = ["link_name", "portfolio"]
