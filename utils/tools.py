import datetime

def longDateToString(n):
  return datetime.datetime.fromtimestamp(n).strftime('%Y-%m-%d %H:%M:%S')