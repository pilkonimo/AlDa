"""ALDA Zettel 1, Aufgabe 2
Max Kahl und Konstantin Neureither"""


'''
a) Es gibt insgesamt 14 Möglichkeiten, die Wochentage auf ein Jahr zu
verteilen. Für jeden der 7 Wochentage gibt es jeweils die Möglichkeit
auf den 01.01. in einem 'gewöhnlichen' und in einem Schaltjahr zu fallen.
'''

from calendar import Calendar, isleap
import datetime


def get_empty_year(leap=False):
    """Creates a list representing a year, elements represent days.

       Elements are lists formatted as [day, month, weekday], where
       weekdays are all set to be 0.
    """
    c = Calendar()
    l = list()
    if leap:
        year = 2020
    else:
        year = 2019
    for month in range(1, 13):
        for day in c.itermonthdays(year, month):
            if day != 0:
                l.append([day, month, 0])
    return l


def count_fridays13(year, begin=0, end=None):
    """Returning occurrences of friday 13th in given year."""
    if end is None:
        end = len(year)
    counter = 0
    for i in range(begin, end):
        if year[i][0] == 13 and year[i][2] == 4:
            counter += 1
    return counter


def run_possibility(startday, leap=False, begin=0, end=None):
    """Returns occurences of friday 13th for specified scenario of a year."""
    # decode weekdays: 0 - monday, 1 - tuesday,..., 4 - friday, ...
    weekday = startday
    year = get_empty_year(leap)
    for i in range(len(year)):
        year[i][2] = weekday
        weekday = (weekday+1) % 7
    return count_fridays13(year, begin, end)


def friday13th():
    """Prints all possible scenarios of a year and corresponding occurences
    of friday 13th.
    """
    print('no leap \n ---------')
    for startday in range(7):
        print('startday:' + str(startday) + '\n' + 'occurrences of friday 13th:' + str(run_possibility(startday)))
    print('leap \n ---------')
    for startday in range(7):
        print('startday:' + str(startday) + '\n' + 'occurrences of friday 13th:' +
              str(run_possibility(startday, leap=True)))


def date_to_index(day, month, year):
    """Converts date to corresponding index in list representation of a year."""
    year_list = get_empty_year(isleap(year))
    for i in range(len(year_list)):
        if year_list[i][0] == day and year_list[i][1] == month:
            return i


def get_startday(year):
    c = Calendar()
    for day in c.itermonthdays2(year, 1):
        if day[0] != 0:
            return day[1]


def friday13thSince(day, month, year):
    """Returns number of friday 13th since specified date."""
    now = datetime.datetime.now()
    if year == now.year:
        return run_possibility(get_startday(year), isleap(year),
                               date_to_index(day, month, year), date_to_index(now.day, now.month, now.year))
    counter = run_possibility(get_startday(year), isleap(year),
                              begin=date_to_index(day, month, year))
    year += 1
    while year < 2019:
        counter += run_possibility(get_startday(year), isleap(year))
        year += 1
    counter += run_possibility(get_startday(year), isleap(year),
                               end=date_to_index(now.day, now.month, now.year))
    return counter


print('Ich habe bereits ' + str(friday13thSince(7, 1, 1998)) + ' Freitage den 13. erlebt.')
