# ONEPTE Exam Practice
OnePTE is a popular platform that helps students get ready for the PTE exam. Students usually use OnePTE by downloading the mobile app or visiting the website. After signing up, they can practice questions and take mock tests. They also receive scores for the answers they submit.

## Features
* Practices more and more questions
* Three types of questions are available

### Question Types
* Summarize Spoken Text (sst)
* Re-Order Paragraph (ro)
* Reading Multiple Choice (rmmcq)


## Details About Some Functions
* `wait_for_db : ` it waits for the postgresql connection.
```
import time

from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to pause execution until database is available"""

    def handle(self, *args, **options):
        """Handle the command"""
        self.stdout.write('Waiting for database...')
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
            except OperationalError:
                self.stdout.write('Database unavailable, waiting 1 second...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!'))
```

* `initialize_question_types : ` Initially to create `Question Type` from existing
```
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

```


## Commands
* Setup
```
docker-compose up --build
```
* Run the web server
```
docker-compose up
```
* Create superuser
```
docker-compose run web sh -c "python manage.py createsuperuser"
```

## Used package
* Django
* Django Rest API
* JWT AUTHENTICATION
* Docker

## Service APIs
* `login :` 
```
api/user/login
```
* `register :` 
```
api/user/register
```
* `List all Question : `
```
api/question/list/
```
* `histories of Answer : `
```
api/question/histories
```
* `Question detail view: ` question_types : `sst`, `ro`, `rmmcq`
```
api/question/detail/<str:question_type>/<str:id>/
```
* `Answer list view (inner Question): `
```
api/question/answer/<int:question__id>/
```
* `Give answer view (inner Answer): `
```
api/question/answer/answer/create/<int:question__id>/
```