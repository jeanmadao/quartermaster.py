def isweekday(date):
    return date.weekday() < 5

def isweekend(date):
    return not isweekday(date)
