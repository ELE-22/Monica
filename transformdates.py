import re
import datetime

regex = '^.* ([0-9]{2}) ([A-Z]{3}).*? ([0-9]{4})$'
dates = list()

def get_Date(wrong_dates):

    for right_dates in wrong_dates:
        date = re.findall(regex,right_dates)
        dates.append("{} {} {}".format(date[0][1].capitalize(), date[0][0], date[0][2]))

    result = list()
    for date_time_str in dates:
        date_time_obj = datetime.datetime.strptime(date_time_str, '%b %d %Y')
        result.append(date_time_obj.date())
    return result


