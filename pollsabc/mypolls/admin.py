from django.contrib import admin
from models import Question,Choices
# Register your models here.

class Qadmin(admin.TabularInline):
    model = Choices
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    inlines = [Qadmin]
    list_display = ['question_text',]

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choices)