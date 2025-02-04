def add_time(start, duration, starting_day=None):
    # Split AM/PM and hours/minutes for start time
    start_time, period = start.split() 
    start_hour, start_min = map(int, start_time.split(':'))

    # Convert start time to 24 hour format
    if period == 'PM' and start_hour != 12:
        start_hour += 12
    elif period == 'AM' and start_hour == 12:
        start_hour = 0
    
    # Split duration hours and min
    duration_hour, duration_min = map(int, duration.split(':'))

    # Find total min
    total_min = start_hour * 60 + start_min + duration_hour* 60 + duration_min

    # Calculate times
    final_hour = (total_min // 60) % 24
    final_min = total_min % 60
    days_later = total_min // (24 * 60)

    
    # Convert back to 12 hour time & update period
    if final_hour < 12:
        period = 'AM'
    else:
        period = 'PM'
    final_hour = final_hour if final_hour != 0 else 12
    if final_hour > 12:
        final_hour -= 12

    # Days of week
    if starting_day:
        days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        day_index = days_of_week.index(starting_day.capitalize())
        new_day = days_of_week[(day_index + days_later) % 7]
    else:
        new_day = None
    
    #formatting
    new_time = f"{final_hour}:{final_min:02d} {period}"
    if new_day:
        new_time += f", {new_day}"
    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"
   
    return new_time
