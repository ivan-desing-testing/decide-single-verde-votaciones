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
            ('H', 'High'),
            ('M', 'Mid'),
            ('L', 'Low'),
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
        if self.value() == 'H':
            return queryset.exclude(preference_isHigh=False)
        if self.value() == 'M':
            return queryset.exclude(preference_isHigh=False)
        if self.value() == 'L':
            return queryset.exclude(preference_isHigh=False)

        else:
            return queryset.all()
