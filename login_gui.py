from tkinter import *
import os
import smtplib
from email.message import EmailMessage
import random
from tkinter import messagebox
import re

root = Tk()

root.geometry('500x555')

Label(root, text='Username', font = ('Times New Roman', 16, 'bold')).place(x=115, y=30)
username_entry = Entry(root, width=45)
username_entry.place(x=115, y=60)

Label(root, text='Password', font = ('Times New Roman', 16, 'bold')).place(x=115, y=110)
password_entry = Entry(root, show='*', width=45)
password_entry.place(x=115, y=140)

def delete_entries():
    username_entry.delete(0, 'end')
    password_entry.delete(0, 'end')

def send_otp():
    username = username_entry.get()
    password = password_entry.get()
    if len(username) == 0 or len(password) == 0:
        messagebox.showwarning('Warning', "Please enter Username or Password!")
    else:
        username_pattern = "\S+@\S+"
        username_result = re.findall(username_pattern, username)
        password_pattern = "^.*(?=.{8,})(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$"
        password_result = re.findall(password_pattern, password)
        if (username_result) and (password_result):
            EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
            EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
            msg = EmailMessage()
            msg['From'] = EMAIL_ADDRESS
            msg['To'] = username    
            msg['Subject'] = 'One Time Password (OTP)'
            msg.set_content(f'To authenticate, please use the following One Time Password (OTP): {random.randint(100000,999999)}')
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                smtp.send_message(msg)

            delete_entries()

            messagebox.showinfo("Information", f"Dear user,\nOne Time Password (OTP) has been sent to your registerd Email-ID. Please check your Email.")
        else:
            messagebox.showwarning("Warning","Invalid Username or Password!!")

Button(root, text='Login', relief = GROOVE, bg='yellow green', fg = 'black', font = ('Times New Roman', 12, 'bold'), padx = 10, command=send_otp).place(x=115, y=200)

Button(root, text='Reset', relief = GROOVE, bg = '#C0C0C0', fg = 'black', font = ('Times New Roman', 12, 'bold'), padx = 10, command=delete_entries).place(x=190, y=200)

root.mainloop()
