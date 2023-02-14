from dataclasses import fields
from django.contrib import admin
from .models import Article, Contact, Comments, Category
from django_summernote.admin import SummernoteModelAdmin

class ArticleAdmin(SummernoteModelAdmin):
    list_display = ('id','title','is_featured','writer','created_date',"status")
    list_display_links = ('id','title','is_featured','writer','created_date')
    prepopulated_fields = {"slug": ("title",)}
    summernote_fields = ('content',)
admin.site.register(Article, ArticleAdmin)

class CommentsAdmin(admin.ModelAdmin):
    list_display = ('id','article','email','message', 'created_date')
    list_display_links = ('id','article','email')
admin.site.register(Comments, CommentsAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','category_name')
    list_display_links = ('id','category_name')
    prepopulated_fields = {"path_alias": ("category_name",)}
admin.site.register(Category, CategoryAdmin)


class InquiryContact(admin.ModelAdmin):
    list_display = ('id','full_name','email','message')
    list_display_links = ('id','full_name','email')
admin.site.register(Contact, InquiryContact)

