from django.urls import path
from .views import (
    Question_SSTDetail,
    Question_RODetail,
    Question_RMMCQDetail,  # Add this line to your URL patterns.
)

app_name = 'api_question'

urlpatterns = [
    path('sst/<int:id>/', Question_SSTDetail.as_view(), name='question_sst_detail'),
    path('ro/<int:id>/', Question_RODetail.as_view(), name='question_ro_detail'),
    path('rmmcq/<int:id>/', Question_RMMCQDetail.as_view(), name='question_rmmcq_detail'),
]