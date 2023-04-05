from tkinter import *


class LoginForm(Frame):
    def __init__(self, user_repo, parent, controller, user_state):
        Frame.__init__(self, parent)
        self.controller = controller
        self.user_repo = user_repo
        self.user_state = user_state
        self.login_frame = Frame(self, bg="light grey")
        self.init_window()

    def login(self, error, username, password):
        user = self.user_repo.check_credentials(username.get(), password.get())
        if user is None:
            error.set("Incorrect username or password")
        else:
            self.user_state.user_id = user.id
            self.controller.show_frame("Header")
            self.controller.show_frame("PlantList")

    def init_window(self):
        self.login_frame.destroy()
        self.login_frame = Frame(self, bg="light grey")
        self.login_frame.pack(side="top", anchor="center")

        username = StringVar()
        password = StringVar()
        error = StringVar()

        # login
        login_label = Label(self.login_frame, text="Sign in", bg="light grey", fg="black", font=("Arial", 16))
        login_label.grid(row=0, column=0, columnspan=2)

      
        username_label = Label(self.login_frame, text="User name", bg="light grey", fg="black", font="Arial")
        username_label.grid(row=1, column=0)
        username_entry = Entry(self.login_frame, textvariable=username, font="Arial, 16", bg="light grey", fg="black")
        username_entry.grid(row=1, column=1)

     
        password_label = Label(self.login_frame, text="Password", bg="light grey", fg="black", font="Arial")
        password_label.grid(row=2, column=0)
        password_entry = Entry(self.login_frame, textvariable=password, show="*", font="Arial, 16", bg="light grey",
                               fg="black")
        password_entry.grid(row=2, column=1)

        # log in button
        login_button = Button(self.login_frame, text="Go!", bg="grey", fg="black", font="Arial, 16",
                              command=lambda: self.login(error, username, password))
        login_button.grid(row=3, column=0, columnspan=2)

        error_message = Label(self.login_frame, textvariable=error, bg="light grey", fg="red", font="Arial")
        error_message.grid(row=4, column=1)

