import re
import dateparser
from datetime import datetime

regex = '^.* ([0-9]{2}) ([A-Z]{3}).*? ([0-9]{4})$'
dates = list()


def get_date(wrong_dates):
    for right_dates in wrong_dates:
        date = re.findall(regex, right_dates)
        dates.append("{} {} {}".format(date[0][1].capitalize(), date[0][0], date[0][2]))

    result = [[], []]
    for date_time_str in dates:
        date_time = dateparser.parse(date_time_str)
        result[0].append(date_time.date())
        today = datetime.now()
        delta = date_time.date() - today.date()
        result[1].append(delta.days)

    return result
