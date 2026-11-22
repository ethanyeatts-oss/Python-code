seconds = int(input("Enter a number of seconds: "))

hours = seconds // 3600

minutes =  (seconds % 3600) / 60

seconds2 = seconds % 60
print(f" That is equal to {hours} hours, {minutes} minutes and {seconds} seconds ")




