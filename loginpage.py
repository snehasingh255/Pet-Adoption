from tkinter import *
import subprocess
import webbrowser
import requests
from tkinter import messagebox as mb
import os 
import sqlite3
   
# --- Database Setup ---
def initialize_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        password TEXT
    )""")
    conn.commit()
    conn.close()

# --- Insert Default User (optional) ---
def add_default_user():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("sneha", "sneha@18"))
        conn.commit()
    except sqlite3.IntegrityError:
        pass  # User already exists
    conn.close()

# --- Validate Login ---
def validate_login(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    result = cursor.fetchone()
    conn.close()
    return result is not None

def signup_page(root):
    if os.path.exists("signuppage.py"):
        subprocess.Popen(["python", "signuppage.py"])
        root.destroy()
    else:
        mb.showinfo("ERROR", "Signup page script not found.")

def update_password_page(frame):
    frame2 = Toplevel(frame)  
    frame2.title("Update Password")
    frame2.attributes('-topmost', True)
    update_head=Label(frame2,text="Update Password", font=("Arial",15))
    new=Label(frame2, text="Enter New Password:", font=("Arial", 15))
    newpass=Entry(frame2, show="*", font=("Arial", 15))
    conpas=Label(frame2, text="Confirm New Password:", font=("Arial", 15))
    confirmpass=Entry(frame2, show="*", font=("Arial", 15))

    update_head.grid(row=0,column=0,columnspan=2, pady=10)
    new.grid(row=1,column=0,padx=10,pady=10)
    newpass.grid(row=1,column=1,padx=10,pady=10)
    conpas.grid(row=2,column=0,padx=10,pady=10)
    confirmpass.grid(row=2,column=1,padx=10,pady=10)
    
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
            # Update password in the database
            conn = sqlite3.connect("users.db")
            cursor = conn.cursor()
            cursor.execute("UPDATE users SET password=? WHERE username=?", (newp, current_user))
            conn.commit()
            conn.close()

            mb.showinfo("Success", "Password updated successfully!")
            frame2.destroy()
    
    save=Button(frame2, text="Save", font=("Arial", 15),command=pass_update)
    save.grid(row=3,column=0,columnspan=2,pady=10)

def login_window():
    def attempt_login():
        username = t1.get().strip()
        password = t2.get().strip()

        if validate_login(username, password):
            mb.showinfo("Login", "Login successful!")
            os.environ["LOGGED_IN_USER"] = username
            subprocess.Popen(["python", "app.py"], env=os.environ)
        else:
            mb.showerror("Login", "Invalid credentials.")

    #if auth.login(username, password):
       # error_label.config(text="Login Successful", fg="green")
        #mb.showinfo("Login", "Login Successful")
        #webbrowser.open(r"C:\Users\Sneha Singh\OneDrive\Desktop\Projects\flask_project\templates\Adoption.html")
    #else:
     #   error_label.config(text="Login Failed", fg="red")
      #  mb.showerror("Login", "Invalid credentials")

    root=Tk()
    root.title("Login Page")
    root.geometry('500x500')
    root.resizable(0,0)
    root.attributes('-topmost', True)
    frame=Frame(root,bg='white')
    frame.grid(sticky="nsew")

    # --- Tkinter Login GUI ---
    login_head=Label(frame,text="LOGIN TO SEE MORE",font=("Times New Roman",15))
    user = Label(frame, text="UserName:", font=("Times New Roman ",15))
    t1 = Entry(frame, font=("Times New Roman",15), width=22)
    pas = Label(frame, text="Password:", font=("Times New Roman ",15))
    t2 = Entry(frame, font=("Times New Roman",15), show="*", width=22)

    forgotbtn=Button(frame,text="Forgot Password?",font=("Times New Roman",15),command=lambda: update_password_page(frame),bd=0,background="white",activebackground="white") 
    loginbtn = Button(frame, text="LOGIN", font=("Times New Roman", 15), command=attempt_login)
    error_label = Label(frame, text="", font=("Times New Roman", 12), fg="red")

    noacc=Label(frame,text="Don't have an account?",font=("Times New Roman",15))
    signbtn=Button(frame,text="Create new account",font=("Times New Roman ",15),command=lambda: signup_page(root),bd=0,background="white",activebackground="white")

    login_head.grid(row=0,column=0, columnspan=2, pady=10)
    user.grid(row=1, column=0, padx=10, pady=10,sticky="w")
    t1.grid(row=1, column=1, padx=10, pady=10, sticky="w")
    pas.grid(row=2, column=0, padx=10, pady=10, sticky="w")
    t2.grid(row=2, column=1, padx=10, pady=10, sticky="w")
    forgotbtn.grid(row=3, column=1, padx=10, pady=10, sticky="nsew")
    loginbtn.grid(row=4, column=0, padx=10, pady=10,columnspan=2)
    error_label.grid(row=5, column=0, columnspan=2, pady=5)
    noacc.grid(row=6, column=0, padx=10, pady=5, sticky="w")
    signbtn.grid(row=6, column=1, pady=5,sticky="nsew")

    root.mainloop()

if __name__ == "__main__":
    initialize_db()
    add_default_user()
    login_window()

