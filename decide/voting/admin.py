from django.contrib import admin
from django.utils import timezone

from .models import QuestionOption
from .models import Question
from .models import Voting

from .filters import StartedFilter


def start(modeladmin, request, queryset):
    for v in queryset.all():
        v.create_pubkey()
        v.start_date = timezone.now()
        v.save()


def stop(ModelAdmin, request, queryset):
    for v in queryset.all():
        v.end_date = timezone.now()
        v.save()


def tally(ModelAdmin, request, queryset):
    for v in queryset.filter(end_date__lt=timezone.now()):
        token = request.session.get('auth-token', '')
        v.tally_votes(token)
        
#A�adiendo acci�n para visualizar como van los votos actualmente sin necesidad de pararlo
def currentTally(ModelAdmin, request, queryset):
    for v in queryset.all():
        token = request.session.get('auth-token', '')
        v.tally_votes(token)           

class QuestionOptionInline(admin.TabularInline):
    model = QuestionOption


class QuestionAdmin(admin.ModelAdmin):
    inlines = [QuestionOptionInline]
    readonly_fields = ('answer', 'option')

    def get_readonly_fields(self, request, obj=None):
    #    def __init__(self, *args, **kwargs):

            if request.models.QuestionOption.TypeAnswer(name="TypeAnswer"=='OPEN').exists():
         #       return self.fields['answer'].widget.attrs['readonly'] = True
                 return  ('answer')

            else:
                return ('option')

       #     if admin.ModelAdmin.value(name="TypeAnswer"=='CLOSED'):
        #         return self.fields['option'].widget.attrs['readonly'] = True

#admin.site.register(Question, QuestionAdmin)


class VotingAdmin(admin.ModelAdmin):
    list_display = ('name','preference', 'start_date', 'end_date')
    readonly_fields = ('start_date', 'end_date', 'pub_key',
                       'tally', 'postproc')
    date_hierarchy = 'start_date'
    list_filter = (StartedFilter,)
    search_fields = ('name', )

    actions = [ start, stop, tally, currentTally ]


admin.site.register(Voting, VotingAdmin)
admin.site.register(Question, QuestionAdmin)
