def add_time(start, duration, start_day=None):
    # Convert start time to 24-hour format
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(":"))
    if period == "PM":
        start_hour += 12

    # Parse duration time
    duration_hour, duration_minute = map(int, duration.split(":"))

    # Calculate total minutes
    total_minutes = start_hour * 60 + start_minute + duration_hour * 60 + duration_minute

    # Calculate days and remaining minutes
    days = total_minutes // (24 * 60)
    remaining_minutes = total_minutes % (24 * 60)

    # Convert back to 12-hour format
    new_hour, new_minute = divmod(remaining_minutes, 60)
    if new_hour >= 12:
        period = "PM"
        if new_hour > 12:
            new_hour -= 12
    elif new_hour == 0:
        new_hour = 12
        period = "AM"
    else:
        period = "AM"

    # Calculate day of the week
    if start_day:
        days_of_week = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
        start_day_index = days_of_week.index(start_day.lower())
        new_day_index = (start_day_index + days) % 7
        new_day = days_of_week[new_day_index]
        if days == 1:
            day_info = " (next day)"
        elif days > 1:
            day_info = f" ({days} days later)"
        else:
            day_info = ""
        return f"{new_hour:02}:{new_minute:02} {period}, {new_day}{day_info}"

    if days == 1:
        day_info = " (next day)"
    elif days > 1:
        day_info = f" ({days} days later)"
    else:
        day_info = ""
    return f"{new_hour:02}:{new_minute:02} {period}{day_info}"

# Pruebas
print(add_time("3:00 PM", "3:10"))  # Debe devolver: 6:10 PM
print(add_time("11:30 AM", "2:32", "Monday"))  # Debe devolver: 2:02 PM, Monday
print(add_time("11:43 AM", "00:20"))  # Debe devolver: 12:03 PM
print(add_time("10:10 PM", "3:30"))  # Debe devolver: 1:40 AM (next day)
print(add_time("11:43 PM", "24:20", "tueSday"))  # Debe devolver: 12:03 AM, Thursday (2 days later)
print(add_time("6:30 PM", "205:12"))  # Debe devolver: 7:42 AM (9 days later)
