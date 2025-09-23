from tkinter import *
from tkinter import messagebox as mb
import subprocess
import os
from werkzeug.security import check_password_hash
import db
from PIL import Image, ImageTk

def update_password_page(frame):
    frame2 = Toplevel(frame)
    frame2.title("Update Password")
    frame2.attributes('-topmost', True)

    update_head = Label(frame2, text="Update Password", font=("Arial", 15))
    new = Label(frame2, text="Enter New Password:", font=("Arial", 15))
    newpass = Entry(frame2, show="*", font=("Arial", 15))
    conpas = Label(frame2, text="Confirm New Password:", font=("Arial", 15))
    confirmpass = Entry(frame2, show="*", font=("Arial", 15))

    update_head.grid(row=0, column=0, columnspan=2, pady=10)
    new.grid(row=1, column=0, padx=10, pady=10)
    newpass.grid(row=1, column=1, padx=10, pady=10)
    conpas.grid(row=2, column=0, padx=10, pady=10)
    confirmpass.grid(row=2, column=1, padx=10, pady=10)

    def pass_update():
        newp = newpass.get().strip()
        conp = confirmpass.get().strip()
        current_user = os.environ.get("LOGGED_IN_USER", None)

        if not newp or not conp:
            mb.showinfo("ERROR", "All fields are required!")
        elif newp != conp:
            mb.showinfo("ERROR", "New Passwords do not match.")
        elif not current_user:
            mb.showinfo("ERROR", "No user is currently logged in.")
        else:
            db.update_user_password(current_user, newp)
            mb.showinfo("Success", "Password updated successfully!")
            frame2.destroy()

    save = Button(frame2, text="Save", font=("Arial", 15), command=pass_update)
    save.grid(row=3, column=0, columnspan=2, pady=10)

def login_window():
    def attempt_login():
        username = t1.get().strip()
        password = t2.get().strip()

        user = db.get_user_by_username(username)
        if user and check_password_hash(user["password"], password):
            os.environ["LOGGED_IN_USER"] = username
            os.environ["USER_ROLE"] = user["role"]
            mb.showinfo("Login", f"Welcome {username}! Role: {user['role'].capitalize()}")

            # Optional: Launch different apps based on role
            if user["role"] == "admin":
                subprocess.Popen(["python", "admin_dashboard.py"], env=os.environ)
            else:
                subprocess.Popen(["python", "app.py"], env=os.environ)
        else:
            mb.showerror("Login", "Invalid credentials.")

    root = Tk()
    root.title("Login Page")
    root.geometry('500x550')
    root.resizable(0, 0)
    root.attributes('-topmost', True)

    frame = Frame(root, bg='#f0f4f7', relief=RAISED)
    frame.pack(fill=BOTH, expand=True, padx=20, pady=20)

    # Load and resize logo
    image = Image.open("C:/Users/Sneha Singh/OneDrive/Desktop/Projects/Adoption_project/static/img/adoptlogo.jpg")
    resized_image = image.resize((200, 100))
    logo = ImageTk.PhotoImage(resized_image)
    logo_label = Label(frame, image=logo, bg='#f0f4f7')
    logo_label.image = logo
    logo_label.grid(row=0, column=0, columnspan=2, pady=(20, 20))

    login_head = Label(frame, text="LOGIN TO SEE MORE", font=("Times New Roman", 18, "bold"),
                       bg='#f0f4f7', fg='#2c3e50')
    login_head.grid(row=1, column=0, columnspan=2, pady=(0, 20))

    user = Label(frame, text="UserName:", font=("Times New Roman", 15), bg='#f0f4f7', fg='#34495e')
    user.grid(row=2, column=0, padx=10, pady=10, sticky="e")
    t1 = Entry(frame, font=("Times New Roman", 15), width=22, bg='white', fg='black', relief=SOLID, bd=1)
    t1.grid(row=2, column=1, padx=10, pady=10, sticky="w")

    pas = Label(frame, text="Password:", font=("Times New Roman", 15), bg='#f0f4f7', fg='#34495e')
    pas.grid(row=3, column=0, padx=10, pady=10, sticky="e")
    t2 = Entry(frame, font=("Times New Roman", 15), show="*", width=22, bg='white', fg='black', relief=SOLID, bd=1)
    t2.grid(row=3, column=1, padx=10, pady=10, sticky="w")

    forgotbtn = Button(frame, text="Forgot Password?", font=("Times New Roman", 13),bg='#f0f4f7', fg='#e74c3c', bd=0,activebackground='#f0f4f7', activeforeground='#c0392b',
                       command=lambda: update_password_page(frame))
    forgotbtn.grid(row=4, column=1, padx=10, pady=5, sticky="e")

    loginbtn = Button(frame, text="LOGIN", font=("Times New Roman", 15),bg='#3498db', fg='white',activebackground='#2980b9', activeforeground='white',
                      command=attempt_login)
    loginbtn.grid(row=5, column=0, columnspan=2, pady=20)

    error_label = Label(frame, text="", font=("Times New Roman", 12), fg="red", bg='#f0f4f7')
    error_label.grid(row=6, column=0, columnspan=2)

    root.mainloop()

if __name__ == "__main__":
    login_window()