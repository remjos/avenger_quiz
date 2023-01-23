import customtkinter

app = customtkinter.CTk()
app.geometry(f"{600}x{500}")
app.title("The Avenger Quiz")


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

def button_event():
    window = customtkinter.CTkToplevel(text="New window")
    window.geometry("600x500")

Frame1 = customtkinter.CTkFrame(master=app, width=200, height=200, corner_radius=10)
Frame1.pack(padx=50, pady=50)

Label1 = customtkinter.CTkLabel(master=app, anchor=customtkinter.CENTER, 
    text="Welcome to the Avenger Quiz", 
    fg_color=("white", "black", ), 
    corner_radius=10)
Label1.place(relx=0.5, rely=0.5, anchor='n')

button2 = customtkinter.CTkButton(master=app, 
    text="Click here to continue to THE AVENGER QUIZ", 
    anchor=customtkinter.CENTER, 
    command=button_event)
button2.pack(padx=5, pady=5)

Frame2 = customtkinter.CTkFrame(master=app)



button1 = customtkinter.CTkButton(master=Frame2, command=button_event)
button1.place(relx=0.5, rely=0.5)


e1 = customtkinter.CTkEntry(master=app, placeholder_text="What is your eye color?")



app.mainloop()
