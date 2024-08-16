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
    class Meta:
        model = Question
        fields = ('id', 'title', 'time_limit', 'audio')



"""________________Re-Order Paragraph (RO) Question Serializer___________________"""
class OptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Options
        fields = ('id', 'title')


class Question_ROSerializer(serializers.ModelSerializer):
    question_options = OptionsSerializer(many=True, read_only=True)
    class Meta:
        model = Question
        fields = ('id', 'title', 'question_options')



"""________________Reading Multiple Choice (Multiple) (RMMCQ)___________________"""



class Question_RMMCQSerializer(serializers.ModelSerializer):
    question_options = OptionsSerializer(many=True, read_only=True)
    class Meta:
        model = Question
        fields = ('id', 'title', 'question_options')


class QuestionListSerializer(serializers.ModelSerializer):
    question_type__title = serializers.CharField(source='question_type.title')
    class Meta:
        model = Question
        fields = ('id', 'title', 'question_type__title')


"""________________Answer Serializer___________________"""

# Answer  serializer
class AnswerSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    class Meta:
        model = Answer
        fields = ('id', 'username', 'answer', 'score')
        read_only_fields = ('username', 'score', 'id',)

    def get_username(self, obj):
        return obj.user.username

