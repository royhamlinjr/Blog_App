from django.contrib import admin
from .models import Post,Category,About

# Customized Post Model
class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('category__name',)
    list_filter = ('category','created_at')
    ordering = ('-created_at',)
    prepopulated_fields = {'slug':('title',)}

# Register your models here.
admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(About)
