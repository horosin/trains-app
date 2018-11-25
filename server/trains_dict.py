from datetime import datetime

trains = [
    {
        'id': "IC0001",
        'start': "Kraków Główny",
        'stations': ['Częstochowa', 'Koluszki', 'Skierniewice'],
        'stop': 'Warszawa Centralna',
        'start_time': datetime.strptime('10:30', '%H:%M'),
        'stations_time': [datetime.strptime('12:15', '%H:%M'), datetime.strptime('12:45', '%H:%M'),
                          datetime.strptime('13:20', '%H:%M')],
        'stop_time': datetime.strptime('13:45', '%H:%M'),
        'duration': '3h 15m',
        'date': '21-11-2018',
        'is_disabled': True,
        'is_children': True,
        'is_quiet': False,
        'is_sleeping': False,
        'is_wars': False,
        'price1': 90,
        'price2': 71

    },
    {
        'id': "IC0002",
        'start': "Kraków Główny",
        'stations': ['Częstochowa', 'Warszawa Zachodnia'],
        'stop': 'Warszawa Centralna',
        'start_time': datetime.strptime('12:45', '%H:%M'),
        'stations_time': [datetime.strptime('15:20', '%H:%M'), datetime.strptime('16:50', '%H:%M')],
        'stop_time': datetime.strptime('17:00', '%H:%M'),
        'duration': '4h 15m',
        'date': '21-11-2018',
        'is_disabled': True,
        'is_children': True,
        'is_quiet': True,
        'is_sleeping': False,
        'is_wars': True,
        'price1': 130,
        'price2': 85

    },
    {
        'id': "IC0003",
        'start': "Kraków Główny",
        'stations': ['Warszawa Centralna'],
        'stop': 'Gdańsk Główny',
        'start_time': datetime.strptime('11:10', '%H:%M'),
        'stations_time': [datetime.strptime('13:55', '%H:%M')],
        'stop_time': datetime.strptime('18:20', '%H:%M'),
        'duration': '7h 10m',
        'date': '21-11-2018',
        'is_disabled': True,
        'is_children': True,
        'is_quiet': True,
        'is_sleeping': False,
        'is_wars': True,
        'price1': 210,
        'price2': 140
    },
    {
        'id': "IC0004",
        'start': "Warszawa Centralna",
        'stations': ['Warszawa Wschodnia', 'Toruń Główny'],
        'stop': 'Gdańsk Główny',
        'start_time': datetime.strptime('14:30', '%H:%M'),
        'stations_time': [datetime.strptime('14:40', '%H:%M'), datetime.strptime('17:45', '%H:%M')],
        'stop_time': datetime.strptime('18:45', '%H:%M'),
        'duration': '4h 15m',
        'date': '21-11-2018',
        'is_disabled': True,
        'is_children': False,
        'is_quiet': False,
        'is_sleeping': True,
        'is_wars': True,
        'price1': 90,
        'price2': 58
    },
    {
        'id': "IC0005",
        'start': "Kraków Główny",
        'stations': ['Częstochowa', 'Koluszki', 'Skierniewice',
                     'Warszawa Centralna', 'Warszawa Wschodnia', 'Toruń Główny'],
        'stop': 'Gdańsk Główny',
        'start_time': datetime.strptime('09:45', '%H:%M'),
        'stations_time': [datetime.strptime('10:20', '%H:%M'), datetime.strptime('11:45', '%H:%M'),
                          datetime.strptime('12:10', '%H:%M'), datetime.strptime('14:50', '%H:%M'),
                          datetime.strptime('17:20', '%H:%M'), datetime.strptime('18:45', '%H:%M')],
        'stop_time': datetime.strptime('19:55', '%H:%M'),
        'duration': '10h 10m',
        'date': '21-11-2018',
        'is_disabled': True,
        'is_children': False,
        'is_quiet': True,
        'is_sleeping': True,
        'is_wars': True,
        'price1': 180,
        'price2': 110
    }
]