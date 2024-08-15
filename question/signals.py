from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from .models import Question_RO
from django.utils.translation import gettext_lazy as _




# Signal implementation for Question_RO
@receiver(pre_save, sender=Question_RO)
def pre_save_question_ro(sender, instance, **kwargs):
    """
    Check the format of the answer field.
    {
    "answer": [[1,2],[2,3],[4,5]]
    }
    """
    if not isinstance(instance.answer, dict):
        raise ValidationError(_("Answer should be a dictionary"))
    if 'answer' not in instance.answer.keys() or len(instance.answer.keys()) != 1:
        raise ValidationError(_("Answer should have a key 'answer'"))
    
    if not isinstance(instance.answer['answer'], list):
        raise ValidationError(_("Answer should be a list"))
    for answer in instance.answer['answer']:
        if not isinstance(answer, list):
            raise ValidationError(_("Answer should be a list of list"))
        if len(answer) != 2:
            raise ValidationError(_("Answer should be a list of list with 2 elements"))
        if not all(isinstance(i, int) for i in answer):
            raise ValidationError(_("Answer should be a list of list with integer elements"))



    instance.answer = instance.answer