#1. Take the number of points one team is ahead.
points_str = input ("Enter the lead in points: ")
points_remaining_int = int(points_str)

#2. Subtract 3
lead_calculation_float = float (points_remaining_int - 3)

#3. Add 0.5 if the team ahead has the ball, else subtract 0.5.
has_ball_str = input ("Does the lead team has the ball (Yes or No): ")

if has_ball_str == 'Yes':
   lead_calculation_float = lead_calculation_float + 0.5
else:
   lead_calculation_float = lead_calculation_float - 0.5
   
#Number less than zero become zero
if lead_calculation_float < 0:
   lead_calculation_float = 0
   
#4. Square the result
lead_calculation_float = lead_calculation_float**2

#5. If the result > number of seconds left, the lead is safe
seconds_remaining_int = int(input("Enter the number of seconds remaining: "))

if lead_calculation_float > seconds_remaining_int:
   print ("Lead is safe.")
else: 
   print ("Lead is not safe.")
   
