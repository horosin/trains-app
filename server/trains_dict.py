trains = [
    {
        'id': "IC0001",
        'start': "Kraków Główny",
        'stations': ['Częstochowa', 'Koluszki', 'Skierniewice'],
        'stop': 'Warszawa Centralna',
        'start_time': '10/30',
        'stations_time': ['12/15', '12/45', '13/20'],
        'stop_time': '13/45',
        'date': '21/11/2018',
        'is_disabled': True,
        'is_children': True,
        'is_quiet': False,
        'is_sleeping': False,
        'is_wars': False

    },
    {
        'id': "IC0002",
        'start': "Kraków Główny",
        'stations': ['Częstochowa', 'Warszawa Centralna'],
        'stop': 'Warszawa Wschodnia',
        'start_time': '12/45',
        'stations_time': ['15/20', '16/50'],
        'stop_time': '17/00',
        'date': '21/11/2018',
        'is_disabled': True,
        'is_children': True,
        'is_quiet': True,
        'is_sleeping': False,
        'is_wars': True

    },
    {
        'id': "IC0003",
        'start': "Kraków Główny",
        'stations': ['Warszawa Centralna'],
        'stop': 'Gdańsk Główny',
        'start_time': '11/10',
        'stations_time': ['13/55'],
        'stop_time': '18/20',
        'date': '21/11/2018',
        'is_disabled': True,
        'is_children': True,
        'is_quiet': True,
        'is_sleeping': True,
        'is_wars': True
    },
    {
        'id': "IC0004",
        'start': "Warszawa Centralna",
        'stations': ['Warszawa Wschodnia', 'Toruń Główny'],
        'stop': 'Gdańsk Główny',
        'start_time': '14/30',
        'stations_time': ['14/40', '17/45'],
        'stop_time': '18/45',
        'date': '21/11/2018',
        'is_disabled': True,
        'is_children': False,
        'is_quiet': False,
        'is_sleeping': True,
        'is_wars': True
    },
    {
        'id': "IC0005",
        'start': "Kraków Główny",
        'stations': ['Częstochowa', 'Koluszki', 'Skierniewice',
                     'Warszawa Centralna', 'Warszawa Wschodnia', 'Toruń Główny'],
        'stop': 'Gdańsk Główny',
        'start_time': '09/45',
        'stations_time': ['10/20', '11/45', '12/10', '14/50', '17/20', '18/45'],
        'stop_time': '19/55',
        'date': '21/11/2018',
        'is_disabled': True,
        'is_children': False,
        'is_quiet': True,
        'is_sleeping': True,
        'is_wars': True
    }
]