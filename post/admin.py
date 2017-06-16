from django.contrib import admin

# Register your models here.


from post.models import Post


def mark_as_draft(modeladmin, request, queryset):
    queryset.update(draft=True)


def mark_as_post(modeladmin, request, queryset):
    queryset.update(draft=False)


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'draft']
    ordering = ['title']
    actions = [mark_as_draft, mark_as_post]


admin.site.register(Post, PostAdmin)
