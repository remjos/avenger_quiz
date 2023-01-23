from tkinter import * 





#tkinter 
#add a message box here to determine if the user want's to contiue with the quiz
#tkinter.messagebox.askquestion(title="Which Avenger ARE you?", message="Would you like to contiue to find out which Avener YOU are?")

root = Tk()
root.title("The Avenger Quiz")

class Page():
    def __init__(self, *args, **kwargs):
        Tk.frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class Page1(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = Tk.Label(self, text="This is page 1")
       entry = Entry(Page1, text="What is your favorite color?")
       entry.get(entry)

       label.pack(side="top")
    

class Page2(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = Tk.Label(self, text="This is page 2")
       label.pack(side="top")

class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = Tk.Label(self, text="This is page 3")
       label.pack(side="top")

class MainView():
    def __init__(self, *args, **kwargs):
        Tk.frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)

        buttonframe = Tk.frame(self)
        container = Tk.frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = Tk.Button(buttonframe, text="Page 1", command=p1.show)
        b2 = Tk.Button(buttonframe, text="Page 2", command=p2.show)
        b3 = Tk.Button(buttonframe, text="Page 3", command=p3.show)

        b1.pack(side="top")
        b2.pack(side="top")
        b3.pack(side="top")

        p1.show()

if __name__ == "__main__":
  
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("400x400")
    root.mainloop()