from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import (
    Audio,
    Question_SST,
    Question_RO,
    Question_RMMCQ,
    Options_RO,
    Options_RMMCQ,
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
        model = Question_SST
        fields = ('id', 'title', 'time_limit', 'audio', 'pre', 'next')

    def get_pre(self, obj):
        """
        Get URL of the previous question.
        """
        pre = Question_SST.objects.filter(id__lt=obj.id).order_by('-id').first()
        return None if pre is None else reverse('api_question:question_sst_detail', kwargs={'id': pre.id}, request=self.context.get('request'))
        # return None if pre is None else pre.id

    def get_next(self, obj):
        """
        Get URL of the next question.
        """
        next = Question_SST.objects.filter(id__gt=obj.id).order_by('id').first()
        # return None if next is None else next.id
        return None if next is None else reverse('api_question:question_sst_detail', kwargs={'id': next.id}, request=self.context.get('request'))
    



"""________________Re-Order Paragraph (RO) Question Serializer___________________"""
class Options_ROSerializer(serializers.ModelSerializer):
    class Meta:
        model = Options_RO
        fields = ('id', 'title')


class Question_ROSerializer(serializers.ModelSerializer):
    options_ro = Options_ROSerializer(many=True, read_only=True)
    # previous_question_url
    pre = serializers.SerializerMethodField()
    # next_question_url
    next = serializers.SerializerMethodField()
    class Meta:
        model = Question_RO
        fields = ('id', 'title', 'options_ro', 'pre', 'next')


    def get_pre(self, obj):
        """
        Get URL of the previous question.
        """
        pre = Question_SST.objects.filter(id__lt=obj.id).order_by('-id').first()
        return None if pre is None else reverse('api_question:question_sst_detail', kwargs={'id': pre.id}, request=self.context.get('request'))
        # return None if pre is None else pre.id

    def get_next(self, obj):
        """
        Get URL of the next question.
        """
        next = Question_SST.objects.filter(id__gt=obj.id).order_by('id').first()
        # return None if next is None else next.id
        return None if next is None else reverse('api_question:question_sst_detail', kwargs={'id': next.id}, request=self.context.get('request'))
    



"""________________Reading Multiple Choice (Multiple) (RMMCQ)___________________"""
class Options_RMMCQSerializer(serializers.ModelSerializer):
    class Meta:
        model = Options_RMMCQ
        fields = ('id', 'title')


class Question_RMMCQSerializer(serializers.ModelSerializer):
    options_rmmcq = Options_RMMCQSerializer(many=True, read_only=True)
    # previous_question_url
    pre = serializers.SerializerMethodField()
    # next_question_url
    next = serializers.SerializerMethodField()
    class Meta:
        model = Question_RMMCQ
        fields = ('id', 'title', 'options_rmmcq', 'pre', 'next')

    def get_pre(self, obj):
        """
        Get URL of the previous question.
        """
        pre = Question_SST.objects.filter(id__lt=obj.id).order_by('-id').first()
        return None if pre is None else reverse('api_question:question_sst_detail', kwargs={'id': pre.id}, request=self.context.get('request'))
        # return None if pre is None else pre.id

    def get_next(self, obj):
        """
        Get URL of the next question.
        """
        next = Question_SST.objects.filter(id__gt=obj.id).order_by('id').first()
        # return None if next is None else next.id
        return None if next is None else reverse('api_question:question_sst_detail', kwargs={'id': next.id}, request=self.context.get('request'))
    






