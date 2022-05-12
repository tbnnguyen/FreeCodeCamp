def add_time(start, duration, day=""):
  # Splitting and storing everything relevant in a variable for later use
  parts = start.split(" ")
  start_time = parts[0]
  ending = parts[1]

  clock_start = start_time.split(":")
  hour_start = clock_start[0]
  min_start = clock_start[1]

  clock_duration = duration.split(":")
  hour_duration = clock_duration[0]
  min_duration = clock_duration[1]

  # Adding minutes and hours with eachother
  new_hour = int(hour_start) + int(hour_duration)
  new_minute = int(min_start) + int(min_duration)

  # Adjust the time when minutes exceeds 60 minutes
  if new_minute > 59:
    hours = new_minute // 60 # true division to only get whole hours
    new_minute = new_minute % 60 # remainder of the minutes not divisible by 60
    new_hour += hours

  days = 0

  # Counter by 12 to able to account for 12 hour clock
  while new_hour > 12:
    if ending == "PM":
      days += 1
      ending = "AM"
    else:
      ending = "PM"
    new_hour -= 12

  # Account for 12 hour transfer
  if new_hour == 12:
    if ending == "AM":
      ending = "PM"
    else:
      days += 1
      ending = "AM"

  days_later = ""

  # Setting amounts of days later where applicable 
  if days == 1:
    days_later = " (next day)"
  elif days > 1:
    days_later = " (" + str(days) + " days later)"

  # Logic for days, setup in a list
  all_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

  new_day = ""
  # Only when new day parameter is used
  if day != "":
    # to fix "broken" input
    index = all_days.index(day.capitalize())
    # Modulo if days is larger than 7 days
    new_index = index + days % 7
    # Resetting index to avoid out of bounds
    if new_index > 6:
      new_index = new_index - 7
    new_day = all_days[new_index]

    # Formatting at the end before return value
    if new_minute < 10:
      new_time = str(new_hour) + ":0" + str(new_minute) + " " + ending + ", " + new_day + days_later
    else:
      new_time = str(new_hour) + ":" + str(new_minute) + " " + ending + ", " + new_day + days_later
  else:
    if new_minute < 10:
      new_time = str(new_hour) + ":0" + str(new_minute) + " " + ending + days_later
    else:
      new_time = str(new_hour) + ":" + str(new_minute) + " " + ending + days_later
  

  return new_time