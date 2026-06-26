def add_time(start, duration):

    start_hour = int(start.split(":")[0])
    star_minuts = int(start.split(":")[1].split()[0])
    end_hour = int(duration.split(":")[0])
    end_minuts = int(duration.split(":")[1].split()[0])
    hour_time = start.split()[1]
    if start_hour >= 13:
        return ("ERROR use the 12-hour clock format (ending in AM or PM)")
    elif star_minuts >= 61 or end_minuts >= 61:
        return ("ERROR use the use only 0 to 60 minuts no more")
    else:
        hour_time_sum = start_hour + end_hour 
        min_time_sum = star_minuts + end_minuts
        if min_time_sum >= 60:
            min_time_sum = min_time_sum - 60
            hour_time_sum = hour_time_sum + 1
        
        new_time = str(hour_time_sum) + ":" +  str(min_time_sum) + " " + hour_time

    return new_time

print(add_time('3:00 PM', '3:10'))
