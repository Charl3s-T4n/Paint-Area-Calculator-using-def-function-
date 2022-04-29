#Write your code below this line 👇
import math    # So that i can use math.ceil() method to round up
def paint_calc(height, weidth, cover):                     # creating def function with input parameters 
  no_of_cans_minimum = (height*width)/cover 
  no_of_cans_rounded = math.ceil(no_of_cans_minimum)       # math.ceil() to round the number up nearest integer 
  print(f"You'll need {no_of_cans_rounded} cans of paint.")          # Using f-string to insert value 

  
#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)                 # Using keyword arguments to input actual value 


