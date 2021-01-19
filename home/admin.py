from django.contrib import admin

from .models import BlogPost


# add the way the data is displayed
class PostBlog(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'slug', 'created_at')
    # list_filter = ("updated_at",) # this filter post by the parameter
    search_fields = ['title', 'content', 'subtitle']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(BlogPost, PostBlog)
