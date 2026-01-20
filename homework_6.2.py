#Number to date converter

user_number = int(input("Enter a seconds from 0 to 8640000: "))

days, remainder = divmod(user_number, 24*60*60)
hours, remainder = divmod(remainder, 60*60)
minutes, seconds = divmod(remainder, 60)

time_str = (
    f"{days} day(s), "
    f"{str(hours).zfill(2)}:"
    f"{str(minutes).zfill(2)}:"
    f"{str(seconds).zfill(2)}"
)

print(time_str)


