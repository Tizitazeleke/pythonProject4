speed = 50
if (24 <= speed < 56):

   print("Speed is normal")
else:
    print("speed is abnormal")


# Task 2: Calories Burned Calculation
calories_per_minute = 4.2
minutes = [10, 15, 20, 25, 30]

print("\nCalories burned on the treadmill:")
for minute in minutes:
    calories_burned = calories_per_minute * minute
    print(f"Calories burned after {minute} minutes: {calories_burned:.2f}")
