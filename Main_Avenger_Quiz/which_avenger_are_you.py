import json
from colors import my_color_list
import time
from avengers_list1 import avenger_list
import sys  
from alpha_bet import american_alphabet
from birthday_month import months_of_the_year
import random

#function to start the quiz questions 

def stop_quiz():
    print("Thanks for playing!\nWe hope to see you again soon!\nPlease leave a review")
    sys.exit()

def quiz():
    while True:
        try:
            q1 = input("What color are your eyes? ").lower()
            q2 = input("What is the first letter of your name? ").lower()
            q3 = input("What month were you born in? ").lower()
            q3 = input("How many letters are in your first name?").lower()
        except ValueError:
            print("Sorry, we did not recognize this input, please try again")
            continue
        else:
            break

            
    list1 = [] #this is to allow the range of first name characters to be assigend to a value
    list2 = [] #this is for the colors list to assign an avenger to it 
    list3 = [] #the list for the birthday_month questions to be stored in 
#todo add more colors to be including 
#question 1 if statements using list 2

    for answer in q1 

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
   
    if 1 or 2 or 3 or 4 in list2 and 1 or 2 or 3 or 4 in list1 and 1 or 2 or 3 or 4 in list3:
        print("The choice is obivious, you are...")
        time.sleep(1) 
        choice = random.choice(avenger_list)
        print(choice)
        print("Now, go live life today acting as", choice)
                        
print("Which Avenger do YOU think you are?")
time.sleep(2)
print("\n")
print("Would you like to find out?")

answer = (input("Y/N: "))
if answer == "Y" or answer == "y":
    quiz()
else:
    time.sleep(1)
    stop_quiz()
 