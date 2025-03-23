print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
combined_name=name1+name2
new_name=combined_name.lower()

t=new_name.count("t")
r=new_name.count("r")
u=new_name.count("u")
e=new_name.count("e")
first_digit=t+r+u+e

l=new_name.count("l")
o=new_name.count("o")
v=new_name.count("v")
e=new_name.count("e")
sec_digit=l+o+v+e


score=int(str(first_digit)+str(sec_digit))

if score<10:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score>=40 and score <=50:
  print(f"Your score is {score}, you are alright together.")
elif score>90:
  print(f"Your score is {score}, you go together like coke and mentos.")
else:
  print(f"Your score is {score}.")