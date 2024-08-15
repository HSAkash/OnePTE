from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import (
    Audio,
    Question_SST,
    Question_RO,
    Question_RMMCQ,
    Options_RO,
    Options_RMMCQ,
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
    # AnswerSerializer
)


# Retrieved details view Question_SST
class Question_SSTDetail(generics.RetrieveAPIView):
    queryset = Question_SST.objects.all()
    serializer_class = Question_SSTSerializer
    lookup_field = 'id'


# Retrieve details view Question_RO
class Question_RODetail(generics.RetrieveAPIView):
    queryset = Question_RO.objects.all()
    serializer_class = Question_ROSerializer
    lookup_field = 'id'


# Retrieve details view Question_RMMCQ
class Question_RMMCQDetail(generics.RetrieveAPIView):
    queryset = Question_RMMCQ.objects.all()
    serializer_class = Question_RMMCQSerializer
    lookup_field = 'id'