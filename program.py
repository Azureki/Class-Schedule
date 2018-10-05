from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import time

from lxml import etree
import datetime
from config import start_date, lesson_time, event
# # print(str(date))

# print(datetime.date(2018, 10, 3))
# print(lesson_time)

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/calendar'


def lesson2event(lessons):
    # type lesson: List[]
    # rtype void
    for time_slice in lessons:
        for i in range(len(time_slice)):
            les = time_slice[i]

            print(les)
            if not les:
                break
            for j in range(0, len(les), 5):
                event['summary'] = les[j + 0]
                event['description'] = les[j + 1]
                # event['attendees'] = [
                # {'email': les[j + 1].replace(',', '+') + '@heu'}]
                event['location'] = les[j + 4]

                # time
                tem = [int(x) for x in les[j + 3][1:-2].split('-')]
                start, end = tem[0], tem[-1]
                start_time = lesson_time[start][0]
                end_time = lesson_time[end][1]
                # event['summary']=summary

                # week
                weeks = les[j + 2][:-3].split(',')
                all_weeks = []
                for week in weeks:
                    tem = week.split('-')  # 取名真头疼
                    all_weeks.extend(
                        list(range(int(tem[0]), int(tem[-1]) + 1)))
                print(all_weeks)

                # print(start, end)

                for week in all_weeks:
                    date = start_date + \
                        datetime.timedelta(days=7 * (week - 1) + i)
                    event['start']['dateTime'] = str(
                        date) + 'T' + start_time + '+08:00'
                    event['end']['dateTime'] = str(
                        date) + 'T' + end_time + '+08:00'
                    service.events().insert(calendarId='primary', body=event).execute()
                    time.sleep(10)

                print(event)
                time.sleep(60)

            # ============

            # process date and time

            #


# 废弃
def lessons2cal(lessons):
    # type lessons: List[List[]]
    # rtype: void

    pass


# with open('Class Schedule.html', 'rb',) as f:
#     html = etree.parse(f)


f = open('Class Schedule.html', 'r', encoding='utf8')  # 为啥不加utf8就报错？不是默认的么？
text = f.read()
# b = text.encode()
f.close()
html = etree.HTML(text)

trs = html.xpath('//tr')
lessons = []
for tr in trs[1:6]:
    time_slice = []
    tds = tr.xpath('./td')
    for td in tds:

        time_slice.append(td.xpath(
            # './/text()')) 很奇怪，text()取得似乎是`><`之间的文本？
            # './div[2]//text()'))
            # ".//text()[translate(normalize-space(),' ','')]"))
            # normalize-space() 似乎不需要
            "./div[2]//text()[translate(.,'\xa0|-','')]"))

    lessons.append(time_slice)


# for time_slice in lessons:
#     for lesson in time_slice:

#         print(lesson)
#     print('----')


# event['summary']='google'
# print(event)

store = file.Storage('token.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('calendar', 'v3', http=creds.authorize(Http()))

lesson2event(lessons)
