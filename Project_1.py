from tkinter import *

def authenticate():
    with open("Login_and_password.txt") as file:
      if login_entry.get() and password_entry.get() in map(str.strip, file):
        result_label.config(text="Success", font=(10))
      else:
        result_label.config(text="Fail", font=(10))

window = Tk()
window.geometry('300x220')
window.title("Authentication")
window.config(bg="#ffffff")

style = {'bg': '#ffffff', 'fg': 'black', 'font': ('Times New Roman', 12), 'relief': 'flat', 'bd': 1}

login_label = Label(window, text="Login:", font=("Times New Roman", 12), bg="#ffffff")
login_label.pack(pady=5)

login_entry = Entry(window, **style)
login_entry.pack(pady=5)

password_label = Label(window, text="Password:", font=("Times New Roman", 12), bg="#ffffff")
password_label.pack(pady=5)

password_entry = Entry(window, show="*", **style)
password_entry.pack(pady=5)

authenticate_btn = Button(window, text="Accept", command=authenticate, font=("Times New Roman", 12), bg="#ffffff", fg="black", bd=0)
authenticate_btn.pack(pady=10)

result_label = Label(window, text="", font=("Times New Roman", 12), bg="#ffffff")
result_label.pack()

window.mainloop()
