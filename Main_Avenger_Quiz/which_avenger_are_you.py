import json
from colors import my_color_list
import time
from avengers_list1 import avenger_list
import sys  
from alpha_bet import american_alphabet
from birthday_month import months_of_the_year
#function to start the quiz questions 

def stop_quiz():
    print("Thanks for playing!" "\n We hope to see you again soon! \n Please leave a review")
    sys.exit()

def quiz():
    while True:
        try:
            q1 = input("What color are your eyes? ").lower()
            q2 = input("What is the first letter of your name? ").lower()
            q3 = input("What month were you born in? ").lower()
        except ValueError:
            print("Sorry, we did not recognize this input, please try again")
            continue
        else:
            break

               #vegtable_list = []
    list1 = [] #this is to allow the range of first name characters to be assigend to a value
    list2 = [] #this is for the colors list to assign an avenger to it 
    list3 = [] #this is the list for the vegtable questions
#todo add more colors to be including 
#question 1 if statements using list 2

    if q1 in my_color_list[0]:
        first_color = 1
        list2.append(first_color)
    if q1 in my_color_list[1]:
        second_color = 2 
        list2.append(second_color)
    if q1 in my_color_list[2]:
        third_color = 3 
        list2.append(third_color)
    if q1 in my_color_list[3]:
        fourth_color = 4 
        list2.append(fourth_color)
#question 2 if statements using list 1
    if q2 in american_alphabet[0:6]:
        first_range = 1
        list1.append(first_range)  
    if q2 in american_alphabet[7:13]:
        second_range = 2
        list1.append(second_range)
    if q2 in american_alphabet[14:20]:
        third_range = 3
        list1.append(third_range)      
    if q2 in american_alphabet[21:26]:
        fourth_range = 4
        list1.append(fourth_range)             
#question 3 if statements using list 3 
    if q3 in months_of_the_year[0:2]:
        first_month_range = 1 
        list3.append(first_month_range)
    if q3 in months_of_the_year[3:5]:
        second_month_range = 2 
        list3.append(second_month_range)
    if q3 in months_of_the_year[6:8]:
        third_month_range = 3
        list3.append(third_month_range)
    if q3 in months_of_the_year[9:11]:
        fourth_month_range = 4
        list3.append(fourth_month_range)
   
    if 1 in list2 and 1 in list1 and 1 in list3:
        print("The choice is obivious, you are...")
        time.sleep(1)
        print(avenger_list[0]) #this prints captain america as avenger
    if 2 in list2 and 2 in list1 and 2 in list3:
        print("The choice is obivious, you are...")
        time.sleep(1)
        print(avenger_list[1]) #this prints iron man as avenger
    if 3 in list2 and 3 in list1 and 3 in list3:
        print("The choice is obivious, you are...")
        time.sleep(1)
        print(avenger_list[2]) #this prints thor as the avenger 
    if 4 in list1 and 4 in list2 and 4 in list3: 
        print("The choice is obivious, you are...")
        time.sleep(1)
        print(avenger_list[3]) #this prints an boodie avenger
    
#todo add the rest of the if statements and determine what avenger should go with what values 
    #elif list2[2] == 3 and list1[2] == 3 and list3[2] == 3:
        #print("The choice is obivious, you are...")
        #time.sleep(1)
        #print(avenger_list[2]) #this prints thor as avenger
            

#question_1_list = my_color_list
#make a fucntion for all the variables of the color names so that the if statement can 
#be based on the color names instead of the values from the dictionary
#def value_color_names():

print("Which Avenger do YOU think you are?")
time.sleep(2)
print("\n")
print("Would you like to find out?")

#def stop_quiz():
 #   print("Thanks for playing!" "\n We hope to see you again soon! \n Please leave a review")
  #  sys.exit()

answer = input("Y/N: ").lower()
if answer == "Y" or "y":
    quiz()
else:
    answer == "N" or "n"
    time.sleep(1)
    print("Thanks for playing \nCome back soon!")
 
#test change 