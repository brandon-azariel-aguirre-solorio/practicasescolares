def add_time(start, duration, start_day=None):

    days = ["Monday", "Tuesday", "Wednesday", "Thursday",
            "Friday", "Saturday", "Sunday"]
    
    start_parts = start.split()
    time = start_parts[0]
    period = start_parts[1]

    start_hour = int(time.split(":")[0])
    start_min = int(time.split(":")[1])

    end_hour = int(duration.split(":")[0])
    end_min = int(duration.split(":")[1])

    if start_hour >= 13:
        return "ERROR use the 12-hour clock format (ending in AM or PM)"
    elif start_min >= 61 or end_min >= 61:
        return "ERROR use the use only 0 to 60 minuts no more"

    if period == "PM" and start_hour != 12:
        start_hour += 12
    elif period == "AM" and start_hour == 12:
        start_hour = 0

    total_start = start_hour * 60 + start_min
    total_duration = end_hour * 60 + end_min

    total = total_start + total_duration

    days_passed = total // (24 * 60)

    total = total % (24 * 60)

    hour24 = total // 60
    minute = total % 60

    if hour24 >= 12:
        period = "PM"
    else:
        period = "AM"

    hour12 = hour24 % 12
    if hour12 == 0:
        hour12 = 12

    if start_day:
        start_day = start_day.capitalize()
        index = days.index(start_day)
        new_day = days[(index + days_passed) % 7]
        new_time = f"{hour12}:{minute:02d} {period}, {new_day}"
    else:
        new_time = f"{hour12}:{minute:02d} {period}"

    if days_passed == 1:
        new_time += " (next day)"
    elif days_passed > 1:
        new_time += f" ({days_passed} days later)"

    return new_time

print(add_time('3:30 PM', '240:12'))



