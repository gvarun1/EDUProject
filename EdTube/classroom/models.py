# django imports
from django.db import models


# non django imports
from accounts.models import Teacher


class Classroom(models.Model):
    which_class = models.CharField(
        max_length=10, null=False, default="Not updated")
    which_section = models.CharField(max_length=3, default='')

    def __str__(self):
        return str(self.which_class)+self.which_section


class Subject(models.Model):
    subject_name = models.CharField(max_length=255)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    teacher_incharge = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject_name


class Chapter(models.Model):
    chapter_name = models.CharField(max_length=255)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.chapter_name


class Concept(models.Model):
    concept_name = models.CharField(max_length=255)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)

    def __str__(self):
        return self.concept_name


class SubConcept(models.Model):
    subconcept_name = models.CharField(max_length=255)
    concept = models.ForeignKey(Concept, on_delete=models.CASCADE)

    def __str__(self):
        return self.subconcept_name


class Tests(models.Model):
    difficulty_choice = (
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),
    )
    test_name = models.CharField(max_length=255, default="Test")
    concept = models.ForeignKey(Concept, on_delete=models.CASCADE)
    max_marks = models.PositiveSmallIntegerField()
    no_of_questions = models.PositiveSmallIntegerField()
    grade_obtained = models.PositiveSmallIntegerField()
    remarks = models.TextField(max_length=250)
    difiiculty = models.CharField(
        max_length=20, choices=difficulty_choice, default='Easy')


class Questions(models.Model):
    difficulty_choice = (
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),
    )
    question_tag = (
        ('Tag1', 'Tag1'),
        ('Tag2', 'Tag2'),
        ('Tag3', 'Tag3'),
        ('Tag4', 'Tag4'),
        ('Tag5', 'Tag5'),
        ('Tag6', 'Tag6'),
        ('Tag7', 'Tag7'),
        ('Tag8', 'Tag8'),

    )
    question_text = models.CharField(max_length=300)
    test = models.ForeignKey(Tests, on_delete=models.CASCADE)
    difiiculty = models.CharField(
        max_length=20, choices=difficulty_choice, default='Easy')
    tag = models.CharField(
        max_length=20, choices=question_tag, default='Tag1')
# class Test(models.Model):
#     subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
#     Class = models.ForeignKey(
#         Classroom, on_delete=models.SET_DEFAULT, default="")
#     no_of_questions = models.PositiveSmallIntegerField()
#     max_marks = models.PositiveSmallIntegerField()
#     grade_obtained = models.PositiveSmallIntegerField()
#     marks_scored = models.SmallIntegerField()
#     remarks = models.TextField(max_length=250)


# class Question(models.Model):
#     test = models.ForeignKey(Test, on_delete=models.CASCADE)
#     question_text = models.CharField(max_length=200)

#     def __str__(self):
#         return self.question_text


class QuestionOptions(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    option_text = models.CharField(max_length=200)
    subconcept = models.ManyToManyField(SubConcept)

    def __str__(self):
        return self.option_text


class Answer(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=200)
    subconcept = models.ManyToManyField(SubConcept)

    def __str__(self):
        return self.answer_text


# class CorrectAnswer(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     correct_option = models.CharField(max_length=1)
#     solution = models.CharField(max_length=500)
