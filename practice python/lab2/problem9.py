name="ram"
age="12"
height=1.8
weight=70
print(f"name of the person: {name}, age: {age}, height in meter: {height}, weight in kg: {weight} ")
BMI=weight/(height**2)
if BMI<=18.5:
  print("underweight")
elif 24.9>BMI>18.5:
  print("healthy weight")
elif 29.9>BMI>25:
  print("overweight")
else :
  print("obese")