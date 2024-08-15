from django.db import models
# use django settings auth user model
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Audio File Upload Location
def upload_location(instance, filename, **kwargs):
    """Upload location for the audio file"""
    # genarate a new filename
    filename = f"{instance.speaker} {filename}"
    return f"audio/{instance.question.title}/{filename}"



# Summarize Spoken Text (SST) Model
class Question_SST(models.Model):
    title = models.CharField(max_length=100)
    time_limit = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Question_SST'
        verbose_name_plural = 'Questions_SST'
        ordering = ['created_at']

    def __str__(self):
        return self.title
    
# Audio File for Summarize Spoken Text
class Audio(models.Model):
    question = models.ForeignKey(Question_SST, on_delete=models.CASCADE, related_name='audio')
    speaker = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    audio = models.FileField(
        upload_to=upload_location, null=False, blank=False
    )


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Audio'
        verbose_name_plural = 'Audios'
        ordering = ['question']

    def __str__(self):
        return f"{self.speaker} - ({self.location})"
    


# Re-Order Paragraph (RO):

class Question_RO(models.Model):
    title = models.CharField(max_length=100)
    answer = models.JSONField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Question_RO'
        verbose_name_plural = 'Questions_RO'
        ordering = ['created_at']

    def __str__(self):
        return self.title
    
# Options for Multiple Choice Questions, Re-Order Paragraph
class Options_RO(models.Model):
    title = models.CharField(max_length=100)
    question = models.ForeignKey(
        Question_RO, on_delete=models.CASCADE, related_name='options_ro')

    class Meta:
        verbose_name = 'Option_RO'
        verbose_name_plural = 'Options_RO'
        ordering = ['question']

    def __str__(self):
        return self.title
    

    

# Reading Multiple Choice (Multiple) (RMMCQ):

class Question_RMMCQ(models.Model):
    title = models.CharField(max_length=100)
    passage = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Question_RMMCQ'
        verbose_name_plural = 'Questions_RMMCQ'
        ordering = ['created_at']

    def __str__(self):
        return self.title
    

# Options for Multiple Choice Questions
class Options_RMMCQ(models.Model):
    title = models.CharField(max_length=100)
    question = models.ForeignKey(
        Question_RMMCQ, on_delete=models.CASCADE, related_name='options_rmmcq')
    is_correct = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Option_RMMCQ'
        verbose_name_plural = 'Options_RMMCQ'
        ordering = ['question']

    def __str__(self):
        return self.title
    


    

"""___________________Answering Models__________________________"""


class Answer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='answers')
    
    # Generic Foreign Key to any Question model
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    question_id = models.PositiveIntegerField()
    question = GenericForeignKey('content_type', 'question_id')
    
    answer = models.TextField()
    score = models.FloatField(default=0.0)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'
        ordering = ['content_type']

    def __str__(self):
        return f"{self.question} - {self.created_at}"
