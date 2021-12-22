from django.contrib import admin

from .models import Choice, Question

admin.site.register(Choice)

#  to customise an admin form (e.g. layout fields) 
#  create a model admin class, then pass it as the 
#  second argument to admin.site.register()
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

admin.site.register(Question, QuestionAdmin)