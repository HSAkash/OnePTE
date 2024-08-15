from django.contrib import admin
from .models import (
    Audio,
    Question_SST,
    Question_RO,
    Question_RMMCQ,
    Options_RO,
    Options_RMMCQ,
    Answer,
)
import admin_thumbnails
from django.core.exceptions import ValidationError
from django.contrib import messages



# Register Question_SST model

@admin_thumbnails.thumbnail('audio', 'speaker', 'location')
class AudioInline(admin.TabularInline):
    """
    Inline class for Audio model.
    Add Audio in Question_SST model in admin panel.(Same page)
    """
    model = Audio
    extra = 1


class AudioAdmin(admin.ModelAdmin):
    list_display = ['id', 'speaker', 'location', 'audio', 'created_at', 'updated_at']
    search_fields = ['speaker', 'location']
    list_filter = ['speaker', 'location']
    list_per_page = 10

admin.site.register(Audio, AudioAdmin)


class Question_SSTAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'time_limit', 'created_at', 'updated_at']
    search_fields = ['title']
    list_filter = ['title']
    list_per_page = 10
    inlines = [AudioInline]

admin.site.register(Question_SST, Question_SSTAdmin)




# Register Question_RO model

@admin_thumbnails.thumbnail('title')
class OptionsRO_Inline(admin.TabularInline):
    """
    Inline class for Options_RO model.
    Add Options in Question_RO model in admin panel.(Same page)
    """
    model = Options_RO
    extra = 1


class Question_ROAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at', 'updated_at']
    search_fields = ['title']
    list_filter = ['title']
    list_per_page = 10
    inlines = [OptionsRO_Inline]

    # Signal implementation for Question_RO
    def save_model(self, request, obj, form, change):
        try:
            super().save_model(request, obj, form, change)
        except ValidationError as e:
            self.message_user(request, str(e), level=messages.ERROR)

admin.site.register(Question_RO, Question_ROAdmin)




# Register Question_RMMCQ model

@admin_thumbnails.thumbnail('title', 'is_correct')
class OptionsRMMCQ_Inline(admin.TabularInline):
    """
    Inline class for Options_RMMCQ model.
    Add Options in Question_RMMCQ model in admin panel.(Same page)
    """
    model = Options_RMMCQ
    extra = 1


class Question_RMMCQAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at', 'updated_at']
    search_fields = ['title']
    list_filter = ['title']
    list_per_page = 10
    inlines = [OptionsRMMCQ_Inline]

admin.site.register(Question_RMMCQ, Question_RMMCQAdmin)



"""___________________Answering Models__________________________"""

# Register Answer model
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'content_type', 'question_id', 'answer', 'created_at']
    search_fields = ['user__username', 'content_type__model', 'question_id']
    list_filter = ['user', 'content_type']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # Example: Add more complex filtering logic here if needed
        return qs

admin.site.register(Answer, AnswerAdmin)