import datetime as dt

def formatted_date():
    today = dt.datetime.now()

    return today.strftime("%A, %d %B %Y")

def formatted_time():
    now_time = dt.datetime.now()

    return now_time.strftime("%H:%M:%S")
