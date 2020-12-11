import datetime

days_or_hours = '12小时'

# t = int(days_or_hours)

try:
    t = int(days_or_hours.split('天')[0])
    days = datetime.datetime.now() + datetime.timedelta(days=t)
except Exception as e:
    t = int(days_or_hours.split('小时')[0])
    days = datetime.datetime.now() + datetime.timedelta(hours=t)
    print(e)

print(days)
