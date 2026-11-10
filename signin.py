#Create a simple banking application 
# The application should be able to allow the user to create an account, 

import customtkinter as ctk
import subprocess
import sqlite3
from CTkMessagebox import CTkMessagebox
import dbconnect

class Bank:
  def __init__(self):
    self.root = ctk.CTk()
    self.root.title("Signin Page")
    self.root.geometry("700x600+0+0")
    self.root.configure(fg_color="#130475")

    ## title 
    self.title_lbl = ctk.CTkLabel(self.root, text="Signin Page", font=("Arial", 35, "bold"), fg_color="#130475", text_color="white", underline=0)
    self.title_lbl.pack(padx=5, pady=10)
    ########


    ## Frame for the inputs ###################################################
    self.frm1 = ctk.CTkFrame(self.root, fg_color="#130475")

    ## input 1, the Username or email label
    self.input1_lbl = ctk.CTkLabel(self.frm1, text="Enter username or email: ", fg_color="#130475", text_color="white", font=("Arial", 25))
    self.input1_lbl.grid(row=0, column=0, padx=10, pady=10)

    ## input 1, the Username or email entry
    self.input1_ent = ctk.CTkEntry(self.frm1, fg_color="white", text_color="black", font=("Arial", 25), width=300)
    self.input1_ent.grid(row=0, column=1, padx=10, pady=10)

    ## input 2, the 4-digit pin label
    self.input2_lbl = ctk.CTkLabel(self.frm1, text="Enter 4 digit pin: ", fg_color="#130475", text_color="white", font=("Arial", 25))
    self.input2_lbl.grid(row=1, column=0, padx=10, pady=20)

    ## input 2, the 4-digit pin entry
    self.input2_ent = ctk.CTkEntry(self.frm1, fg_color="white", text_color="black", font=("Arial", 25), width=100)
    self.input2_ent.grid(row=1, column=1, padx=10, pady=20)

    self.frm1.pack(padx=10, pady=10)
    #############################################################################


    ## Signin button
    self.signin_btn = ctk.CTkButton(self.root, text="Signin", fg_color="white", text_color="black", hover_color="green", font=("Arial", 30), command = self.signin)
    self.signin_btn.pack(padx=10, pady=30)

    ## signup option label
    self.signup_lbl = ctk.CTkLabel(self.root, text="Don't have an account?", font=("Arial", 25), fg_color="#130475", text_color="white")
    self.signup_lbl.pack(padx=10, pady=(50, 0))

    ## signup option button
    self.signup_opt = ctk.CTkButton(self.root, text="Signup", fg_color="black", text_color="white", hover_color="green", font=("Arial", 18), command = self.signup)
    self.signup_opt.pack(padx=10)


    ## credit
    self.credit = ctk.CTkLabel(self.root, text="MADE BY ANJI", fg_color="#130475", text_color="dark grey", font=("Arial", 15))
    self.credit.pack(padx=10, pady=50)


    self.root.mainloop()

  ## signin button function #####################
  def signin(self):
    name_or_email = self.input1_ent.get().strip()
    pin = self.input2_ent.get().strip()
    
    
    if not pin or not name_or_email:
      CTkMessagebox(title="Error", message="Enter all inputs to sign in")

    elif not pin.isdigit():
      CTkMessagebox(title="Error", message="Pin must be numerical values")

    elif len(pin) != 4:
      CTkMessagebox(title="Error", message="Pin length must be 4")

    else:
      try:
        con = sqlite3.connect('bank.db')
        cur = con.cursor()

        cur.execute("""
            SELECT *
            FROM users
            WHERE (username LIKE ? OR email LIKE ?)
            AND pin = ?
        """, (name_or_email, name_or_email, pin))

        result = cur.fetchone()
        con.close()

        if result:
          try:
            subprocess.Popen([
            "python",
            "main.py",
            str(result[1]),
            str(result[2]),
            str(result[3]),
            str(result[4])
        ])

            self.root.destroy()

          except Exception as e:
            CTkMessagebox(title="Error", message=str(e))
        else:
            CTkMessagebox(title="Error", message="Invalid user, please Sign Up")

      except Exception as e:
          CTkMessagebox(title="Error", message=str(e))
    ##############################################

  ## signup button function #####################
  def signup(self):
    subprocess.Popen(["python","signup.py"])
    self.root.destroy()
  ##############################################

Bank()