from django.contrib import admin
from .models import BlogPost
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

class BlogPostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = BlogPost
        fields = '__all__'

class BlogPostAdmin(admin.ModelAdmin):
    form = BlogPostAdminForm
    list_display = ('title', 'created_at', 'updated_at')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)

admin.site.register(BlogPost, BlogPostAdmin)
