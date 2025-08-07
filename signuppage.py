from tkinter import *
import subprocess
from tkinter import messagebox as mb

registered_users = []
def validate_signup():
    name=t1.get().strip()
    username=t2.get().strip()
    passwd=t3.get().strip()
    confirmpass=t4.get().strip()

    if not name or not username or not passwd or not confirmpass:
        mb.showinfo("ERROR", "All fields are required!")
        return
    
    if username in registered_users:
        mb.showinfo("ERROR", "Username already taken! Please choose another.")
        return
    
    if passwd != confirmpass:
        mb.showinfo("ERROR", "Passwords do not match!")
        return
    
    mb.showinfo("Success", "Account created successfully!")

    # Add the new username to the "database"
    registered_users.append(username)
    print(registered_users)  #to check
    
def login_pg():
    try:
        subprocess.Popen(["python", "loginpage.py"]) 
        root.destroy()
    except subprocess.CalledProcessError:
        mb.showinfo("ERROR", "Login page couldn't be opened.")

root =Tk()
root.title("Sign Up")
root.geometry('500x500') 
root.attributes('-topmost', True)

frame1=Frame(root,bg="white")
frame1.grid(sticky="nsew")
signup_head=Label(frame1,text="SIGN UP",font=("Times New Roman",15))
name=Label(frame1,text="Full Name:",font=("Times New Roman",15))
t1=Entry(frame1,font=("Times New Roman",15))
username=Label(frame1,text="Username:",font=("Times New Roman",15))
t2=Entry(frame1,font=("Times New Roman",15))
passwd=Label(frame1,text="Password:",font=("Times New Roman",15))
t3=Entry(frame1,font=("Times New Roman",15))
confirmpass=Label(frame1,text="Confirm Password",font=("Times New Roman",15))
t4=Entry(frame1,font=("Times New Roman",15))

signup_head.grid(row=0,column=0, columnspan=2, pady=10)
name.grid(row=1,column=0, padx=10, pady=10, sticky="w")
t1.grid(row=1,column=1, padx=10, pady=10, sticky="w")
username.grid(row=2,column=0, padx=10, pady=10, sticky="w")
t2.grid(row=2,column=1, padx=10, pady=10, sticky="w")
passwd.grid(row=3,column=0, padx=10, pady=10, sticky="w")
t3.grid(row=3,column=1, padx=10, pady=10, sticky="w")
confirmpass.grid(row=4,column=0, padx=10, pady=10, sticky="w")
t4.grid(row=4,column=1, padx=10, pady=10, sticky="w")

signinbtn=Button(frame1,text="SIGN UP",font=("Times New Roman",15),command=validate_signup)
signinbtn.grid(row=5,column=0, padx=10,pady=10,columnspan=2,sticky="sew")
loginbtn=Button(frame1,text="BACK TO LOGIN",font=("Times New Roman",15),command=login_pg)
loginbtn.grid(row=6,column=0, padx=10,pady=10,columnspan=2,sticky="sew")

root.mainloop()