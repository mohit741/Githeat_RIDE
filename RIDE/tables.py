import django_tables2 as tables


class station_table(tables.Table):

    class Meta:
        template_name = 'bootstrap-responsive.html'
        fields = (
            'No.',
            'Stations name',
            'Arrives',
            'Departs',
            'Stop time',
            'Distance travelled',
            'Day',
            'Route',
        )

