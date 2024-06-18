import tkinter as tk
import random
import string

def password():
    password = entry.get()
    password_var. set(password)

window = tk.Tk()
window.title("password generator")

entry = tk.Entry(window,show="*")
entry.pack(pady=10)

generate_button = tk.Button(window,text = "generate password",command = password)
generate_button.pack(pady=10)
password_var = tk.StringVar()

password_label = tk.Label(window,textvariable = password_var,font=("Helvetica",16),bg="grey",padx=50,pady=5)
password_label.pack(pady = 10)

window.mainloop()








    
