import customtkinter

app = customtkinter.CTk()
app.geometry(f"{600}x{500}")
app.title("The Avenger Quiz")


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

Frame1 = customtkinter.CTkFrame(master=app, width=500, height=500, corner_radius=10)
Frame1.pack(padx=50, pady=50)
Label1 = customtkinter.CTkLabel(master=app, text="Welcome to the Avenger Quiz", fg_color=("white", "black"), corner_radius=10)
Label1.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

Frame2 = customtkinter.CTkFrame(master=app)

def button_event():
    print("button pressed")

button1 = customtkinter.CTkButton(master=Frame2)



e1 = customtkinter.CTkEntry(master=app, placeholder_text="What is your eye color?")





app.mainloop()
