from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .models import (
    Question,
    Answer,
)

from rest_framework import (
    generics,
    permissions,
    status,
    filters,
    pagination
)

from .serializers import (
    Question_SSTSerializer,
    # AudioSerializer,
    Question_ROSerializer,
    # Options_ROSerializer,
    Question_RMMCQSerializer,
    # Options_RMMCQSerializer,
    # AnswerSerializer,
    QuestionListSerializer
)


# Retrieved details view Question_SST
class Question_SSTDetailView(generics.RetrieveAPIView):
    queryset = Question.objects.filter(question_type__title='sst')
    serializer_class = Question_SSTSerializer
    lookup_field = 'id'


# Retrieve details view Question_RO
class Question_RODetailView(generics.RetrieveAPIView):
    queryset = Question.objects.filter(question_type__title='ro')
    serializer_class = Question_ROSerializer
    lookup_field = 'id'


# Retrieve details view Question_RMMCQ
class Question_RMMCQDetailView(generics.RetrieveAPIView):
    queryset = Question.objects.filter(question_type__title='rmmcq')
    serializer_class = Question_RMMCQSerializer
    lookup_field = 'id'

# List questions view
class QuestionListView(generics.ListAPIView):
    serializer_class = QuestionListSerializer
    queryset = Question.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('question_type',)




