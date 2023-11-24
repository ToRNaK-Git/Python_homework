user_integer = int(input('Please enter your integer from 0 to 8640000: '))
x_days = user_integer // (24 * 60 * 60)
x_hours = user_integer // (60 * 60) - (x_days * 24)
x_mins = (user_integer // 60) - (x_days * 24 * 60) - (x_hours * 60)
x_secs = user_integer - (x_days * 24 * 60 * 60) - (x_hours * 60 * 60) - (x_mins * 60)
ending = ''
if x_days % 10 == 1 and x_days != 11:
    ending = 'день'
elif 2 <= x_days % 10 <= 4 and x_days != 12 and x_days != 13 and x_days != 14:
    ending = 'дні'
else:
    ending = 'днів'
x_hours = str(x_hours).zfill(2)
x_mins = str(x_mins).zfill(2)
x_secs = str(x_secs).zfill(2)
print(f"{x_days} {ending}, {x_hours}:{x_mins}:{x_secs}")
