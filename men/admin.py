from django.contrib import admin

from .models import *


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date')
    fields = ('question_text', 'user', 'cat')
    readonly_fields = ('pub_date', )


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Question, QuestionAdmin)
admin.site.register(Category, CategoryAdmin)
