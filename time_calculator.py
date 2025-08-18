def add_time(start, duration, starting_day=None):
    # Days of the week
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    # Split start time into time and AM/PM
    time, period = start.split()
    hour, minute = map(int, time.split(':'))

    # Convert start time to 24-hour format
    if period == 'PM' and hour != 12:
        hour += 12
    elif period == 'AM' and hour == 12:
        hour = 0

    # Parse duration
    dur_hour, dur_minute = map(int, duration.split(':'))

    # Add duration to start time
    final_minute = minute + dur_minute
    final_hour = hour + dur_hour + final_minute // 60
    final_minute = final_minute % 60
    total_days_later = final_hour // 24
    final_hour = final_hour % 24

    # Convert back to 12-hour format
    new_period = 'AM'
    if final_hour >= 12:
        new_period = 'PM'
    if final_hour > 12:
        final_hour -= 12
    elif final_hour == 0:
        final_hour = 12

    # Build the result string
    new_time = f"{final_hour}:{final_minute:02d} {new_period}"

    # Add day of the week if provided
    if starting_day:
        start_day_index = days.index(starting_day.capitalize())
        new_day_index = (start_day_index + total_days_later) % 7
        new_day = days[new_day_index]
        new_time += f", {new_day}"

    # Add day indicator
    if total_days_later == 1:
        new_time += " (next day)"
    elif total_days_later > 1:
        new_time += f" ({total_days_later} days later)"

    return new_time
