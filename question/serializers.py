from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import (
    QuestionType,
    Audio,
    Question,
    Options,
    Answer,
)


"""________________Summarize Spoken Text (SST) Question Serializer___________________"""


# Audio Serializer 
class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audio
        fields = ('id', 'question', 'speaker', 'location', 'audio')

class Question_SSTSerializer(serializers.ModelSerializer):
    audio = AudioSerializer(many=True, read_only=True)
    # previous_question_url
    pre = serializers.SerializerMethodField()
    # next_question_url
    next = serializers.SerializerMethodField()
    class Meta:
        model = Question
        fields = ('id', 'title', 'time_limit', 'audio', 'pre', 'next')

    def get_pre(self, obj):
        """
        Get URL of the previous question.
        """
        pre = Question.objects.filter(id__lt=obj.id, question_type__title='sst').order_by('-id').first()
        return None if pre is None else reverse('api_question:question_sst_detail', kwargs={'id': pre.id}, request=self.context.get('request'))
        # return None if pre is None else pre.id

    def get_next(self, obj):
        """
        Get URL of the next question.
        """
        next = Question.objects.filter(id__gt=obj.id, question_type__title='sst').order_by('id').first()
        # return None if next is None else next.id
        return None if next is None else reverse('api_question:question_sst_detail', kwargs={'id': next.id}, request=self.context.get('request'))
    



"""________________Re-Order Paragraph (RO) Question Serializer___________________"""
class OptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Options
        fields = ('id', 'title')


class Question_ROSerializer(serializers.ModelSerializer):
    question_options = OptionsSerializer(many=True, read_only=True)
    # previous_question_url
    pre = serializers.SerializerMethodField()
    # next_question_url
    next = serializers.SerializerMethodField()
    class Meta:
        model = Question
        fields = ('id', 'title', 'question_options', 'pre', 'next')


    def get_pre(self, obj):
        """
        Get URL of the previous question.
        """
        pre = Question.objects.filter(id__lt=obj.id, question_type__title='ro').order_by('-id').first()
        return None if pre is None else reverse('api_question:question_sst_detail', kwargs={'id': pre.id}, request=self.context.get('request'))
        # return None if pre is None else pre.id

    def get_next(self, obj):
        """
        Get URL of the next question.
        """
        next = Question.objects.filter(id__gt=obj.id, question_type__title='ro').order_by('id').first()
        # return None if next is None else next.id
        return None if next is None else reverse('api_question:question_sst_detail', kwargs={'id': next.id}, request=self.context.get('request'))
    



"""________________Reading Multiple Choice (Multiple) (RMMCQ)___________________"""



class Question_RMMCQSerializer(serializers.ModelSerializer):
    question_options = OptionsSerializer(many=True, read_only=True)
    # previous_question_url
    pre = serializers.SerializerMethodField()
    # next_question_url
    next = serializers.SerializerMethodField()
    class Meta:
        model = Question
        fields = ('id', 'title', 'question_options', 'pre', 'next')

    def get_pre(self, obj):
        """
        Get URL of the previous question.
        """
        pre = Question.objects.filter(id__lt=obj.id, question_type__title='rmmcq').order_by('-id').first()
        return None if pre is None else reverse('api_question:question_sst_detail', kwargs={'id': pre.id}, request=self.context.get('request'))
        # return None if pre is None else pre.id

    def get_next(self, obj):
        """
        Get URL of the next question.
        """
        next = Question.objects.filter(id__gt=obj.id, question_type__title='rmmcq').order_by('id').first()
        # return None if next is None else next.id
        return None if next is None else reverse('api_question:question_sst_detail', kwargs={'id': next.id}, request=self.context.get('request'))
    


class QuestionListSerializer(serializers.ModelSerializer):
    question_type__title = serializers.CharField(source='question_type.title')
    class Meta:
        model = Question
        fields = ('id', 'title', 'question_type__title')