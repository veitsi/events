from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import feedparser


def index(request):
    events = ['Kyiv Outsourcing Forum 2017, 26 — 27 травня, Київ',
                   'Открытый видеоурок "Как стать тестировщиком ПО и зарабатывать от $500 и больше в месяц", 10 марта',
                   'Xamarin / .NET / Azure Kyiv Meetup #1, 14 March, Kyiv',
                   'Курсы по тестированию ПО для начинающих (Online). Открытый первый урок, 9 марта',
                   'Drupal Camp Kyiv 2017, 10 — 11 июня, Киев',
                   'Лекция "Что такое UI/UX дизайн? Hard\'n\'Soft skills", 15 марта, Одесса',
                   'Курс IT English, 11 березня, Київ',
                   'IT talk: Outsourced systems development in financial markets: why does it matter?, 16 March, Dnipro',
                   'Курс .NET/C#-Pro, 15 березня, Київ', 'MeetUp "SQL Server: XML vs JSON", 18 марта, Харьков',
                   'Вебинар "Почему аналитика звонков нужна малому бизнесу и как её подключить по цене ужина в ресторане на двоих", 10 марта',
                   'English training "General speaking style and ways of saying "no"", 14 марта, Днепр',
                   'iForum-2017, 25 мая, Киев',
                   'Вебинар "Business Analyst Toolkit: Подготовка к собеседованию на позицию junior/middle BA", 6 марта',
                   'Kharkov AI Club #19 - Neural networks on mobile, F-transform, CV for parking, 18 марта, Харьков',
                   'Kievfprog 2017.1, 18 March, Kyiv', 'Розмовний клуб з ІТ English. Зустріч #1, 15 березня, Луцьк',
                   'Практикум Елены Рыжковой «Статус и эффективность: править или управлять?», 15 марта, Киев',
                   'Наверняка HR марафон #2, 23 марта, Киев',
                   'Открытая лекция "Разработка больших Web-приложений на PHP", 6 марта, Харьков']

    template = loader.get_template('events/index.html')
    return HttpResponse(template.render({'events':events}, request))


# Create your views here.

if __name__ == '__main__':
    d = feedparser.parse('https://dou.ua/calendar/feed/')
    event = d['entries'][0]
    events = []
    print(d['entries'][0].keys(), len(d['entries']), event.keys())
    for event in d['entries']:
        events.append(event.title)
    print(events)
