from django.contrib import admin

# Register your models here.
from post.models import Post, Replies, Comments, UserResponse

admin.site.register(Post)
admin.site.register(Comments)
admin.site.register(Replies)
admin.site.register(UserResponse)