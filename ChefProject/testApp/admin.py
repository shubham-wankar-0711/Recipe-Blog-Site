from django.contrib import admin
from testApp.models import Post, Comment

# Register your models here.


class PostAdmin(admin.ModelAdmin):

    list_display = ['id','category','title', 'slug', 'author','user_detail','body',
                    'publish', 'created', 'updated', 'status', 'image','user_image']
    list_filter = ['publish', 'author', 'created']
    search_fields = ('title', 'body')
    date_hierarchy = 'publish'
    raw_id_fields = ('author',)
    ordering = ['status', 'publish']
    prepopulated_fields = {'slug': ('title',)}


class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'body',
                    'post', 'created', 'updated', 'active']
    list_filter = ('created', 'name', 'active')
    search_fields = ('name', 'created', 'body')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
