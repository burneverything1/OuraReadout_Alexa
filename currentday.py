from datetime import datetime
from pytz import timezone
tz = timezone('EST')

def gettime():
  return datetime.now(tz)