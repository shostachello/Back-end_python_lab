from django.contrib import admin

from category.models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'slug')
    prepopulated_fields = {'slug': ('category',)}
    fieldsets = (('', {
        'fields': ('category',),
    }),
                 ((u'Додатково'), {
                     'classes': ('grp-collapse grp-closed',), 'fields': ('slug',),
                 }),
                 )


admin.site.register(Category, CategoryAdmin)