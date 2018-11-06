import datetime


# 开学日期
start_date = datetime.date(2018, 9, 3)


# 上课时间，共13节
lesson_time = [
    ['08:00:00', '08:00:00'],  # 占位
    ['08:00:00', '08:45:00'],
    ['08:50:00', '09:35:00'],
    ['09:55:00', '10:40:00'],
    ['10:45:00', '11:30:00'],
    ['11:35:00', '12:20:00'],

    ['13:30:00', '14:15:00'],
    ['14:20:00', '15:05:00'],
    ['15:25:00', '16:10:00'],
    ['16:15:00', '17:00:00'],
    ['17:05:00', '17:50:00'],

    ['18:30:00', '19:15:00'],
    ['19:20:00', '20:05:00'],
    ['20:10:00', '20:55:00'],
]

event = {
    'summary': '',
    'location': '',
    'description': '',
    'start': {
        'dateTime': '2018-10-02T09:00:00+08:00',
        'timeZone': 'Asia/Shanghai',
    },
    'end': {
        'dateTime': '2018-10-02T17:00:00+08:00',
        'timeZone': 'Asia/Shanghai',
    },
    # 'recurrence': [
    #     'RRULE:FREQ=DAILY;COUNT=2'
    # ],
    'attendees': [
        # {'email': '@heu'},
    ],
    'reminders': {
        'useDefault': True,
        # 'overrides': [
        #     # {'method': 'email', 'minutes': 24 * 60},
        #     # {'method': 'popup', 'minutes': 10},
        # ],
    },
}

# >>> import datetime
# datetime.date(2018, 10, 2)
# >>> str(datetime.date(2018,10,2))
# >>> datetime.date(2018,10,2)+datetime.timedelta(days=7*5)
# http://www.wklken.me/posts/2015/03/03/python-base-datetime.html#datetime-date
