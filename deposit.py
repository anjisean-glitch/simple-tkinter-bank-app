#Create a simple banking application 
# The application should be able to allow the user to create an account, 

import customtkinter as ctk
import subprocess
import sqlite3
from CTkMessagebox import CTkMessagebox
import dbconnect
import sys

## variables gotten from the subprocess Popen code inside the deposit function inside the main.py
username = sys.argv[1]
email = sys.argv[2]
pin = sys.argv[3]
amount = sys.argv[4]
#####################################################################

class Bank:
  def __init__(self):
    self.root = ctk.CTk()
    self.root.title(f"Deposit Page/{username}")
    self.root.geometry("700x600+0+0")
    self.root.configure(fg_color="#130475")

    ## title #########################
    self.title = ctk.CTkLabel(self.root, text="WELCOME TO THE DEPOSIT PAGE", font=("Arial", 40, "bold"), fg_color="#130475", text_color="white", underline=0)
    self.title.pack(padx=10, pady=20)
    ##################################

    ## frame for deposit ##############
    self.frm = ctk.CTkFrame(self.root, fg_color="#130475")

    self.que_lbl = ctk.CTkLabel(self.frm, text="How much would you like to deposit: ", font=("Arial", 25), fg_color="#130475", text_color="white")
    self.que_lbl.grid(row=0, column=0)

    self.deposit_amt = ctk.CTkEntry(self.frm, font=("Arial", 25), fg_color="white", text_color="black")
    self.deposit_amt.grid(row=0, column=1)

    self.frm.pack(padx=10, pady=10)
    ###################################

    ## deposit button ####################
    self.deposit_btn = ctk.CTkButton(self.root, text="DEPOSIT", font=("Arial", 30), fg_color="black", text_color="white", hover_color="green", command=self.deposit)
    self.deposit_btn.pack(padx=10, pady=20)
    ######################################

    ## back to main option label
    self.main_lbl = ctk.CTkLabel(self.root, text="Go Back To Main Page?", font=("Arial", 25), fg_color="#130475", text_color="white")
    self.main_lbl.pack(padx=10, pady=(50, 0))
    
    ## back to main option button
    self.main_pg = ctk.CTkButton(self.root, text="Back", fg_color="black", text_color="white", hover_color="green", font=("Arial", 18), command = self.back)
    self.main_pg.pack(padx=10)

    ## credit
    self.credit = ctk.CTkLabel(self.root, text="MADE BY ANJI", fg_color="#130475", text_color="dark grey", font=("Arial", 15))
    self.credit.pack(padx=10, pady=50)

    self.root.mainloop()

  ## deposit function
  def deposit(self):
    deposit_amt = self.deposit_amt.get().strip()
    if not deposit_amt:
      CTkMessagebox(title="Error", message="Please fill the space!")
      
    elif not deposit_amt.isdigit():
      CTkMessagebox(title="Error", message="Deposit amount must be numerical values!")

    elif float(deposit_amt) <100:
      CTkMessagebox(title="Error", message="Deposit amount must be higher than 100!")
    
    
    else:

      try:
        con = sqlite3.connect('bank.db')
        cur = con.cursor()

        cur.execute('''UPDATE users SET amount = ?
                    WHERE username = ?''',(float(amount) + float(deposit_amt), username))

        con.commit()

        cur.execute('''
                    SELECT amount FROM users
                    WHERE username = ?
                    ''', (username,))
        self.new_balance = cur.fetchone()[0]

        con.close()

        msg = CTkMessagebox(title="Info", message=f"You have successfully deposited! \nCurrent Balance: ${self.new_balance}", icon="info")
        msg.get()

        self.back()

      except Exception as e:
        CTkMessagebox(title="Error", message=str(e))

      


  ## back to main function
  def back(self):
    try:
      subprocess.Popen([
        "python",
        "main.py",
        username,
        email,
        pin,
        str(getattr(self, "new_balance", amount))
        ])

      self.root.destroy()

    except Exception as e:
      CTkMessagebox(title="Error", message=str(e))
 

Bank()