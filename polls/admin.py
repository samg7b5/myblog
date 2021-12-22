from django.contrib import admin

from .models import Choice, Question

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

#  to customise an admin form (e.g. layout fields) 
#  create a model admin class, then pass it as the 
#  second argument to admin.site.register()
class QuestionAdmin(admin.ModelAdmin):

	# defines Question overview
	list_display = ('question_text', 'pub_date', 'was_published_recently')
	list_filter = ['pub_date']
	search_fields = ['question_text']

	# defines drilldown
	fieldsets = [
		(None,               {'fields': ['question_text']}),
		('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
	]
	inlines = [ChoiceInline]



admin.site.register(Question, QuestionAdmin)