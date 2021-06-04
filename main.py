# error handling task done by Mikayla
from tkinter import *
from tkinter import messagebox
# tkinter body
root = Tk()
root.geometry("500x300")
root.title("Authentification")
root.config(bg="#34495e")
# heading
heading = Label(root, fg="white", bg="#34495e", text="Please enter your login credentials:", font=("Helvetica", 15, "bold"))
heading.place(relx=0.17, rely=0.14)
# frame
frame = Frame(root,bg="#34495e")
frame.place(relx=0.33, rely=0.3)
# username label and entry
username = Label(frame, bg="#34495e", fg="white", text="Username:", font=("Helvetica", 11))
username.pack()
user_entry = Entry(frame)
user_entry.pack()
# password entry and label
password = Label(frame, fg="white", bg="#34495e", text="Password:", font=("Helvetica", 11))
password.pack()
password_entry = Entry(frame, show="*")
password_entry.pack()
# login function
def login():
    # username entries allowed
    username_options = {"Mikayla": "1212", "Ashley":"2158", "Liesl":"2398", "Chrislyn":"8551"}
    if username_options.get(user_entry.get()):
        if username_options[user_entry.get()] == password_entry.get():
            root.destroy()
            import error_handling
        else:
            messagebox.showerror("Login Details","Please enter valid login credentials." )
            user_entry.delete(0, END)
            password_entry.delete(0, END)
# login button
login_btn = Button(root, borderwidth=3, text="Login", padx=15, pady=10, bg="#2e4053", fg="white", command=login, font=("Helvetica", 10, "bold"))
login_btn.place(relx=0.42, rely=0.7)

root.mainloop()