from django.contrib.admin import SimpleListFilter


class StartedFilter(SimpleListFilter):
    title = 'started'
    parameter_name = 'started'

    def lookups(self, request, model_admin):
        return [
            ('NS', 'Not started'),
            ('S', 'Started'),
            ('R', 'Running'),
            ('F', 'Finished'),
        ]

    def queryset(self, request, queryset):
        if self.value() == 'NS':
            return queryset.filter(start_date__isnull=True)
        if self.value() == 'S':
            return queryset.exclude(start_date__isnull=True)
        if self.value() == 'R':
            return queryset.exclude(start_date__isnull=True).filter(end_date__isnull=True)
        if self.value() == 'F':
            return queryset.exclude(end_date__isnull=True)


        else:
            return queryset.all()
class ThemeFilter(SimpleListFilter):
    title = 'themeVotation'  
    parameter_name = 'themeVotation'
    
    def lookups(self, request, model_admin):
        return [
              ('El', 'Electoral'),
              ('Si', 'Self-interest'),
              ('Kw', 'Knowledge'),
              ('Ts', 'Testing'),
              ('Su', 'Survey'),

        ] 

    def queryset(self, request, queryset): 
        if self.value() == 'El':
            return queryset.exclude(themeVotation ='Si').exclude(themeVotation ='Kw').exclude(themeVotation ='Ts').exclude(themeVotation ='Su')
        if self.value() == 'Si':
            return queryset.exclude(themeVotation ='El').exclude(themeVotation ='Kw').exclude(themeVotation ='Ts').exclude(themeVotation ='Su')
        if self.value() == 'Kw':
            return queryset.exclude(themeVotation ='El').exclude(themeVotation ='Si').exclude(themeVotation ='Ts').exclude(themeVotation ='Su')
        if self.value() == 'Ts':
            return queryset.exclude(themeVotation ='El').exclude(themeVotation ='Si').exclude(themeVotation ='Kw').exclude(themeVotation ='Su')
        if self.value() == 'Su':
            return queryset.exclude(themeVotation ='El').exclude(themeVotation ='Si').exclude(themeVotation ='Kw').exclude(themeVotation ='Ts')

        else:
            return queryset.all()     

class PreferenceFilter(SimpleListFilter):
    title = 'preference'  
    parameter_name = 'preference'
    
    def lookups(self, request, model_admin):
        return [
            ('H', 'High'),
            ('M', 'Mid'),
            ('L', 'Low'),
        ] 

    def queryset(self, request, queryset): 
        if self.value() == 'H':
            return queryset.exclude(preference ='M').exclude(preference ='L') 
        if self.value() == 'M':
            return queryset.exclude(preference ='H').exclude(preference ='L') 
        if self.value() == 'L':
            return queryset.exclude(preference ='H').exclude(preference ='M') 

        else:
            return queryset.all()     
