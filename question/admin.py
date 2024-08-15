from django.contrib import admin
from .models import (
    Audio,
    Question_SST,
    Question_RO,
    Question_RMMCQ,
    Options_RO,
    Options_RMMCQ,
)
import admin_thumbnails



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
    list_display = ['speaker', 'location', 'audio', 'created_at', 'updated_at']
    search_fields = ['speaker', 'location']
    list_filter = ['speaker', 'location']
    list_per_page = 10

admin.site.register(Audio, AudioAdmin)


class Question_SSTAdmin(admin.ModelAdmin):
    list_display = ['title', 'time_limit', 'created_at', 'updated_at']
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
    list_display = ['title', 'created_at', 'updated_at']
    search_fields = ['title']
    list_filter = ['title']
    list_per_page = 10
    inlines = [OptionsRO_Inline]

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
    list_display = ['title', 'created_at', 'updated_at']
    search_fields = ['title']
    list_filter = ['title']
    list_per_page = 10
    inlines = [OptionsRMMCQ_Inline]

admin.site.register(Question_RMMCQ, Question_RMMCQAdmin)
