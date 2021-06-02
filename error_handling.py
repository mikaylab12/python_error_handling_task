from tkinter import *
from tkinter import messagebox
window = Tk()
window.geometry("400x300")
window.title("Error Handling:")
window.config(bg="#2e4053")
# label and entry
amount_label = Label(window, fg="white", bg="#2e4053", text="Please enter the amount in your account")
amount_label.place(relx=0.16, rely=0.2)
amount_entry = Entry(window)
amount_entry.place(relx=0.28, rely=0.35)
# function
def check_funds():
    amount = amount_entry.get()
    try:
        amount = int(amount)
        if amount >= 3000:
            messagebox.showinfo("Status Feedback", "Congratulations:\nYou qualify for Malaysia!")
        else:
            messagebox.showinfo("Status Feedback", "Please deposit more funds for the excursion")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid input")
# check button
check_btn = Button(window, text="Check Amount", bg="#2e4053", fg="white", borderwidth=5, padx=15, pady=10, command=check_funds)
check_btn.place(relx=0.31, rely=0.5)
window.mainloop()
