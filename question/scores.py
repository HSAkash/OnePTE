import random
from .models import Question
def scoreSST(user_answer):
    scores = [0.0,0.5,1.0,1.5,2.0]
    Content = scores[random.randint(0,len(scores)-1)]
    Form = scores[random.randint(0,len(scores)-1)]
    Grammar = scores[random.randint(0,len(scores)-1)]
    Vocabulary = scores[random.randint(0,len(scores)-1)]
    Spelling = scores[random.randint(0,len(scores)-1)]
    return f"""
Content: {Content}
Form: {Form}
Grammar: {Grammar}
Vocabulary: {Vocabulary}
Spelling: {Spelling}
totally: {Content+Form+Grammar+Vocabulary+Spelling}
"""


def scoreRO(true_answer, user_answer):
    true_answer = true_answer.split(',')
    user_answer = user_answer.split(',')
    true_answer = [x.strip() for x in true_answer]
    user_answer = [x.strip() for x in user_answer]
    true_answer_pairs = [(true_answer[i], true_answer[i+1]) for i in range(0, len(true_answer)-1, 1)]
    user_answer_pairs = [(user_answer[i], user_answer[i+1]) for i in range(0, len(user_answer)-1, 1)]
    score = 0
    for pair in user_answer_pairs:
        if pair in true_answer_pairs:
            score += 1
            true_answer_pairs.remove(pair)
    
    return f"{score}"


def scoreRMMCQ(question, user_answer):
    user_answer = user_answer.lower().split(',')
    user_answer = [x.strip() for x in user_answer]
    options = question.question_options.all()
    true_answer = [option.title.strip()[0].lower() for option in options if option.is_correct]
    score = 0
    for user_choice in user_answer:
        if user_choice in true_answer:
            score += 1
            true_answer.remove(user_choice)
        else:
            score -= 1
    score = score if score >= 0 else 0
    return f"{score}"


def get_score(user_answer, question_id):
    question = Question.objects.get(id=question_id)
    question_type = question.question_type.title
    if question_type == 'sst':
        return scoreSST(user_answer)
    elif question_type== 'ro':
        return scoreRO(question.answer, user_answer)
    elif question_type == 'rmmcq':
        return scoreRMMCQ(question, user_answer)