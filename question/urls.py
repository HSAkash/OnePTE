from django.urls import path
from .views import (
    Question_SSTDetailView,
    Question_RODetailView,
    Question_RMMCQDetailView,
    QuestionListView,
)

app_name = 'api_question'

urlpatterns = [
    path('sst/<int:id>/', Question_SSTDetailView.as_view(), name='question_sst_detail'),
    path('ro/<int:id>/', Question_RODetailView.as_view(), name='question_ro_detail'),
    path('rmmcq/<int:id>/', Question_RMMCQDetailView.as_view(), name='question_rmmcq_detail'),
    path('list/', QuestionListView.as_view(), name='question_list'),  # List all questions
]