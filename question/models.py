from django.db import models
# use django settings auth user model
from django.conf import settings

# Audio File Upload Location
def upload_location(instance, filename, **kwargs):
    """Upload location for the audio file"""
    # genarate a new filename
    filename = f"{instance.speaker} {filename}"
    return f"audio/{instance.question.title}/{filename}"


class QuestionType(models.Model):
    title = models.CharField(max_length=100, unique=True, blank=False, null=False)
    full_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.title} - {self.full_name}"


# Question model
class Question(models.Model):
    question_type = models.ForeignKey(
        QuestionType, on_delete=models.CASCADE, related_name='question_type', blank=True)
    title = models.CharField(max_length=100)
    time_limit = models.IntegerField(blank=True, null=True)
    answer = models.CharField(max_length=100, blank=True, null=True)
    passage = models.TextField(max_length=1000, blank=True, null=True)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'
        ordering = ['created_at']

    def __str__(self):
        return self.title
    
# Audio File for Summarize Spoken Text
class Audio(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='audio')
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
    



    
# Options for Multiple Choice Questions, Re-Order Paragraph
class Options(models.Model):
    title = models.CharField(max_length=100)
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='question_options')
    is_correct = models.BooleanField(default=False)
    class Meta:
        verbose_name = 'Option'
        verbose_name_plural = 'Options'
        ordering = ['question']

    def __str__(self):
        return self.title
    


"""___________________Answering Models__________________________"""


class Answer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    answer = models.TextField(max_length=1000, blank=True, null=True)
    score = models.CharField(max_length=100, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'

    def __str__(self):
        return f"{self.question} - {self.created_at}"
