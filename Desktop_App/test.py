import customtkinter
import json
from colors import my_color_list
import time
from avengers_list1 import avenger_list
import sys  
from alpha_bet import american_alphabet
from birthday_month import months_of_the_year
import random

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("The Avenger Quiz")
        self.geometry(f"{600}x{500}")

    def button_event1():
        dialog1 = customtkinter.CTkInputDialog(text= "What color are your eyes?", title="Question 1")
        answer1 = dialog1.get_input()
        answer1 = customtkinter.StringVar(value=answer1)
        
        dialog2 = customtkinter.CTkInputDialog(text="What is the first letter of your name?", title="Question 2")
        answer2 = dialog2.get_input()
        answer2 = customtkinter.StringVar(value=answer2)
        
        dialog3 = customtkinter.CTkInputDialog(text="What month where you born in?", title="Question 3")
        answer3 = dialog3.get_input()
        answer3 = customtkinter.StringVar(value=answer3)
    
        dialog4 = customtkinter.CTkInputDialog(text="How many letters are in your first name?", title="Question 4")
        answer4 = dialog4.get_input()
        answer4 = customtkinter.StringVar(value=answer4)

        label1 = customtkinter.CTkLabel(master=app, textvariable=answer1, width=10, height=5)
        label1.pack()

        label2 = customtkinter.CTkLabel(master=app, textvariable=answer2, width=10, height=5)
        label2.pack()

        label3 = customtkinter.CTkLabel(master=app, textvariable=answer3, width=10, height=5)
        label3.pack()

        label4 = customtkinter.CTkLabel(master=app, textvariable=answer4, width=10, height=5)
        label4.pack()

        list1 = []

        if answer1 == "test".lower():
            list1.append(answer1)

    def button_creation(button_event1):
        Label1 = customtkinter.CTkLabel(master=app, anchor=customtkinter.CENTER, 
            text="Welcome to the Avenger Quiz",
            corner_radius=10)
        Label1.place(relx=0.5, rely=0.5, anchor='n')

        button2 = customtkinter.CTkButton(master=app, 
            text="Click here to continue to THE AVENGER QUIZ", 
            anchor=customtkinter.CENTER, 
            command=button_event1)
        button2.pack(padx=5, pady=5)

        Frame2 = customtkinter.CTkFrame(master=app)

        Frame1 = customtkinter.CTkFrame(master=app, width=200, height=200, corner_radius=10)
        Frame1.pack(padx=50, pady=50)

app = App()
app.mainloop()