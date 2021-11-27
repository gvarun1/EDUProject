from django.contrib import admin

from .models import Classroom, Subject,  Chapter, Concept, SubConcept, Tests, Questions, Answer, QuestionOptions

# Register your models here.
admin.site.register(Classroom)
admin.site.register(Subject)
# admin.site.register(Test)
# admin.site.register(Question)
# admin.site.register(Choice)
# admin.site.register(CorrectAnswer)
admin.site.register(Chapter)
admin.site.register(Concept)
admin.site.register(SubConcept)
admin.site.register(Tests)
admin.site.register(Questions)
admin.site.register(Answer)
admin.site.register(QuestionOptions)
