def add_time(start, duration, startDay = False):
  weekdays = [ 'monday',
               'tuesday',
               'wednesday',
               'thursday',
               'friday',
               'saturday',
               'sunday']

  
  days = 0
  
  hours, mins = start.split(":")
  mins, period = mins.split(" ")
  dHrs, dMin = duration.split(":")

  hours = int(hours)
  mins = int(mins)
  dHrs = int(dHrs)
  dMin = int(dMin)
  period = period.strip().lower()

  totalHours = hours + dHrs
  totalMin = mins + dMin
  

  if totalMin >= 60:
    totalHours += int(totalMin / 60)
    totalMin = int(totalMin % 60)

  hoursLeft = totalHours
  
  if totalHours >= 24:
    days += int(totalHours / 24)
    hoursLeft = totalHours % 24

  if period == "pm" and hoursLeft >= 12:
    days += 1
    period = "am"
    hoursLeft = hoursLeft % 12

  if period == "am" and hoursLeft >= 12:
    period = "pm"
    hoursLeft = hoursLeft % 12

  if hoursLeft == 0:
    hoursLeft = 12

  result = f'{hoursLeft}:{totalMin:02} {period.upper()}'
  if startDay:
    startDay = startDay.strip().lower()
    selectDay = int((weekdays.index(startDay) + days) % 7)
    endDay = weekdays[selectDay]
    result += f', {endDay.title()} {getDaysLater(days)}'
    
  else:
    result = " ".join((result, getDaysLater(days)))
  

  return result.strip()

def getDaysLater(days):
  if days == 1:
    return "(next day)"
  elif days > 1:
    return f"({days} days later)"
  return ""