from django.urls import path
from .views import (
    QuestionDetailView,
    QuestionListView,
    HistoryAnswerListView,
    QuestionAnswerListView,
    AnswerCreateView,
)

app_name = 'api_question'

urlpatterns = [
    
    path('detail/<str:question_type>/<str:id>/', QuestionDetailView.as_view(), name='question_detail'),
    path('answer/create/<int:question__id>/', AnswerCreateView.as_view(), name='answer_create'),
    path('answer/<int:question__id>/', QuestionAnswerListView.as_view(), name='question_answer_list'),
    path('list/', QuestionListView.as_view(), name='question_list'),  # List all questions
    path('history/', HistoryAnswerListView.as_view(), name='history_answer_list'), 
]