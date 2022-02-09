from tkinter import *
from tkinter import messagebox
import random
import string


symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
def create_password():
    password_entry.delete(0, END)
    password = [random.choice(string.ascii_letters).lower() for i in range(3)]
    password += [str(random.randint(0,9)) for i in range(4)]
    password += [random.choice(string.ascii_letters).upper() for i in range(3)]
    password += [random.choice(symbols) for i in range(4)]
    random.shuffle(password)
    password = "".join(password)
    password_entry.insert(0, password)
    


def add_password():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you have entered the website")
    elif len(email) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you have entered your email")
    elif len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you have entered your password or generate a password")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nWebsite: {website}\nEmail: {email} "
                                                      f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


  
window = Tk()
window.title("Password Manager")
window.config(padx=80, pady=80)


#Labels
name_label = Label(text="Password Manager", font=("Arial", 25))
name_label.grid(row=0, column=1)
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW")
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
password_entry = Entry(width=26)
password_entry.grid(row=3, column=1, sticky="EW")


# Buttons
generate_password_button = Button(text="Generate Password", command=create_password)
generate_password_button.grid(row=3, column=2, sticky="EW")
add_button = Button(text="Add", width=36, command=add_password)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()




