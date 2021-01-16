from django.contrib import admin
from django.utils import timezone

from .models import QuestionOption
from .models import Question
from .models import Voting

from .filters import StartedFilter
from .filters import PreferenceFilter
from .filters import ThemeFilter

from import_export import resources
from import_export.admin import ImportExportModelAdmin

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
def importTallyToFile(ModelAdmin, request, queryset):
    for v in queryset.all():
        token = request.session.get('auth-token', '')
        v.tally_to_file(token)


def export(ModelAdmin, request, queryset):
    dataset = VotingResource().export()
    print(dataset.csv)

class QuestionOptionInline(admin.TabularInline):
    model = QuestionOption


class QuestionAdmin(admin.ModelAdmin):
    inlines = [QuestionOptionInline]


class VotingResource(resources.ModelResource):

    class Meta:
        model = Voting
        fields = ('id', 'name', 'postproc',)

class VotingAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('name', 'themeVotation', 'preference', 'start_date', 'end_date')
    readonly_fields = ('start_date', 'end_date', 'pub_key',
                       'tally', 'postproc')
    date_hierarchy = 'start_date'
    list_filter = (StartedFilter, ThemeFilter, PreferenceFilter)
    search_fields = ('name', )

    actions = [ start, stop, restart, tally, currentTally, importTallyToFile ,export]

    resource_class = VotingResource



admin.site.register(Voting, VotingAdmin)
admin.site.register(Question, QuestionAdmin)
