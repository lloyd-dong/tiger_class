# BMI = kg/(m * m)
# https://www.nhlbi.nih.gov/health/educational/lose_wt/BMI/bmi-m.htm
height = input("Your height is (m): ")
weight = input("Your wight is (kg): ")

# ver1
# BMI = weight / (height * height)
# print("Your BMI is " + BMI) # wrong

# ver2  
# BMI = int(weight) / (int(height) * int(height))
# print("Your BMI is " + str(BMI)) #BMI 0

# ver3  
# BMI = float(weight) / (float(height) * float(height))
# print("Your BMI is " + str(BMI))

# ver4 google squre, round
BMI = float(weight) / pow(float(height),2)
print("Your BMI is " + str(round(BMI,2)))


if BMI <= 18.5 :
  print("Your are too weak!")
elif BMI > 18.5 and BMI < 25 :
  print("You are in good shape")
elif BMI >= 25 and BMI < 30 :
  print("You are overweight !")
else:
  print("you are too fat !")