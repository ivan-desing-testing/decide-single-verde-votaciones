from django.contrib import admin
from django.utils import timezone

from .models import QuestionOption
from .models import Question
from .models import Voting

from .filters import StartedFilter
from .filters import PreferenceFilter
from .filters import ThemeFilter
from .filters import ScopeFilter


def start(modeladmin, request, queryset):
    for v in queryset.all():
        v.create_pubkey()
        v.start_date = timezone.now()
        v.save()

def stop(ModelAdmin, request, queryset):
    for v in queryset.all():
        v.end_date = timezone.now()
        v.save()

def restart(ModelAdmin, request, queryset):
    for v in queryset.all():
        v.end_date = None
        v.save()

def tally(ModelAdmin, request, queryset):
    for v in queryset.filter(end_date__lt=timezone.now()):
        token = request.session.get('auth-token', '')
        v.tally_votes(token)
        
#Anadiendo accion para visualizar como van los votos actualmente sin necesidad de pararlo
def currentTally(ModelAdmin, request, queryset):
    for v in queryset.all():
        token = request.session.get('auth-token', '')
        v.tally_votes(token)

#Accion para importar el tally a un txt y lo comprime en un zip
def exportTallyToFile(ModelAdmin, request, queryset):
    for v in queryset.all():
        token = request.session.get('auth-token', '')
        v.tally_to_file(token)

class QuestionOptionInline(admin.TabularInline):
    model = QuestionOption


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('desc','scopes',)
    list_filter = (ScopeFilter,)
    inlines = [QuestionOptionInline]

class VotingAdmin(admin.ModelAdmin):
    list_display = ('name', 'themeVotation', 'preference', 'start_date', 'end_date')
    readonly_fields = ('start_date', 'end_date', 'pub_key',
                       'tally', 'postproc')
    date_hierarchy = 'start_date'
    list_filter = (StartedFilter, ThemeFilter, PreferenceFilter)
    search_fields = ('name', )

    actions = [ start, stop, restart, tally, currentTally, exportTallyToFile]




admin.site.register(Voting, VotingAdmin)
admin.site.register(Question, QuestionAdmin)
