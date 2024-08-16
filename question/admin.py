from django.contrib import admin
from .models import (
    QuestionType,
    Question,
    Answer,
    Audio,
    Options,
)
import admin_thumbnails
from django.core.exceptions import ValidationError
from django.contrib import messages


# Register QuestionType model

class QuestionTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'full_name']
    search_fields = ['title', 'full_name']
    list_per_page = 10


admin.site.register(QuestionType, QuestionTypeAdmin)



@admin_thumbnails.thumbnail('audio', 'speaker', 'location')
class AudioInline(admin.TabularInline):
    """
    Inline class for Audio model.
    Add Audio in  model in admin panel.(Same page)
    """
    model = Audio
    extra = 1


# Register Question_RO model

@admin_thumbnails.thumbnail('title')
class Options_Inline(admin.TabularInline):
    """
    Inline class for Options model.
    Add Options in Question model in admin panel.(Same page)
    """
    model = Options
    extra = 1



class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'question_type']
    search_fields = ['title']
    list_filter = ['question_type']
    list_per_page = 10
    inlines = [AudioInline, Options_Inline]

admin.site.register(Question, QuestionAdmin)




"""___________________Answering Models__________________________"""

# Register Answer model
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', "question__id", 'question', 'score',]
    search_fields = ['user__username', 'question_title']
    list_filter = ['user', 'question']

admin.site.register(Answer, AnswerAdmin)