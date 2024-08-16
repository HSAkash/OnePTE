from django.core.management.base import BaseCommand
from question.models import QuestionType

class Command(BaseCommand):
    help = 'Initialize QuestionType objects'

    def handle(self, *args, **kwargs):
        question_types = [
            {'title': 'sst', 'full_name': 'Summarize Spoken Text'},
            {'title': 'ro', 'full_name': 'Re-Order Paragraph'},
            {'title': 'rmmcq', 'full_name': 'Reading Multiple Choice'},
            # Add more types as needed
        ]

        for qt in question_types:
            QuestionType.objects.get_or_create(title=qt['title'], defaults={'full_name': qt['full_name']})
        self.stdout.write(self.style.SUCCESS('Successfully initialized QuestionType objects'))
