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
    filters,
    pagination
)

from .serializers import (
    Question_SSTSerializer,
    Question_ROSerializer,
    Question_RMMCQSerializer,
    QuestionListSerializer,
    AnswerSerializer
)

from .scores import get_score

# List questions view
class QuestionListView(generics.ListAPIView):
    serializer_class = QuestionListSerializer
    queryset = Question.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('question_type',)


# Retrieve details view Question
class QuestionDetailView(generics.RetrieveAPIView):
    queryset = Question.objects.all()

    def get_object(self):
        question_type = self.kwargs.get('question_type')
        question_id = self.kwargs.get('id')
        return get_object_or_404(Question, question_type__title=question_type, id=question_id)
    def get_serializer_class(self):
        question_type = self.kwargs.get('question_type')
        if question_type == 'sst':
            return Question_SSTSerializer
        elif question_type == 'ro':
            return Question_ROSerializer
        elif question_type == 'rmmcq':
            return Question_RMMCQSerializer


"""____________________Answers Views_________________________"""

# Answers List view
class HistoryAnswerListView(generics.ListAPIView):
    serializer_class = AnswerSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    search_fields = ('question__title', 'user__username')
    pagination_class = pagination.PageNumberPagination
    page_size = 10
    permission_classes = [permissions.IsAuthenticated,]
    filterset_fields = ('question__question_type',)

    def get_queryset(self):
        # filter by user
        queryset = Answer.objects.filter(user=self.request.user)
        return queryset
    


# Retrieve Answer view based on Question_id
class QuestionAnswerListView(generics.ListAPIView):
    serializer_class = AnswerSerializer
    pagination_class = pagination.PageNumberPagination
    page_size = 10

    def get_queryset(self):
        # filter by question
        queryset = Answer.objects.filter(question_id=self.kwargs.get('question__id'))
        return queryset




# Create Answer view based on Question
class AnswerCreateView(generics.CreateAPIView):
    serializer_class = AnswerSerializer
    permission_classes = [permissions.IsAuthenticated,]

    def perform_create(self, serializer):
        # Get user's score 
        score = get_score(self.request.data.get('answer'), self.kwargs.get('question__id'))

        serializer.save(user=self.request.user,score=score, question_id=self.kwargs.get('question__id'))





