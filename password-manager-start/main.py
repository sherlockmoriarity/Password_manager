from tkinter import*
from tkinter import messagebox
# ------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    getwebsite = website_entry.get()
    getemail = email_entry.get()
    getpassword = password_entry.get()

    if len(getwebsite) == 0 or len(getpassword) == 0:
        messagebox.showinfo(title="...........", message="fill in the information")
    else:
        if_ok = messagebox.askokcancel(title= getwebsite, message= f"these are the details , check them :"
                                                        f"\nEmail:{getemail}\n password={getpassword} \n "
                                                        f"is is ok to save them ?")
        if if_ok:
            with open("data.txt", mode="a") as file:
                file.write(f"{getwebsite} | {getemail} | {getpassword}\n")
                website_entry.delete(0,END)
                password_entry.delete(0,END)


# ---------------------------- UI SETUP ----------------------w--------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0,column=1)

web_name = Label(text="Website")
web_name.grid(row=1,column=0,sticky="w")
email = Label(text="Email/Username")
email.grid(row=2,column=0,sticky="w")
password = Label(text="Password")
password.grid(row=3,column=0,sticky="w")

website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(row=1,column=1,columnspan= 2,sticky="w")
email_entry = Entry(width= 35)
email_entry.grid(row=2,column=1,columnspan= 2,sticky="w")
email_entry.insert(0,"xzxzxzx@gmail.com")
password_entry = Entry(width= 21)
password_entry.grid(row=3,column=1)


generate_password_button= Button(text="Generate Password")
generate_password_button.grid(row=3,column=2)
add_button= Button(text= "Add",width= 36,command=save)
add_button.grid(row=4,column=1,columnspan= 2)


window.mainloop()