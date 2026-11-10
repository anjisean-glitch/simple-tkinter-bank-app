#Create a simple banking application 
# The application should be able to allow the user to create an account, 

import customtkinter as ctk
import subprocess
import sqlite3
from CTkMessagebox import CTkMessagebox
import sys

## variables gotten from the subprocess Popen code inside the withdraw function inside the main.py
username = sys.argv[1]
email = sys.argv[2]
pin = sys.argv[3]
amount = sys.argv[4]
######################################################################

class Bank:
  def __init__(self):
    self.root = ctk.CTk()
    self.root.title(f"Withdraw Page/{username}")
    self.root.geometry("900x600+0+0")
    self.root.configure(fg_color="#130475")

    ## Title#######
    self.title = ctk.CTkLabel(self.root, text="WELCOME TO THE WITHDRAW PAGE", font=("Arial", 40, "bold"), fg_color="#130475", text_color="white", underline=0)
    self.title.pack(padx=10, pady=20)
    ###############

    ## frame for withdrawal ######################
    self.frm = ctk.CTkFrame(self.root, fg_color="#130475")

    self.que_lbl = ctk.CTkLabel(self.frm, text="How much would you like to withdraw: ", font=("Arial", 25), fg_color="#130475", text_color="white")
    self.que_lbl.grid(row=0, column=0)

    self.withdraw_amt = ctk.CTkEntry(self.frm, font=("Arial", 25), fg_color="white", text_color="black")
    self.withdraw_amt.grid(row=0, column=1)

    self.frm.pack(padx=10, pady=10)
    ##############################################


    ## withdraw button #########
    self.withdraw_btn = ctk.CTkButton(self.root, text="WITHDRAW", font=("Arial", 30), fg_color="black", text_color="white", hover_color="green", command=self.withdraw)
    self.withdraw_btn.pack(padx=10, pady=20)
    ############################

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

  ## withdraw function ########################
  def withdraw(self):
    withdraw_amt = self.withdraw_amt.get().strip()
    if not withdraw_amt:
      CTkMessagebox(title="Error", message="Please fill the space!")
      
    elif not withdraw_amt.isdigit():
      CTkMessagebox(title="Error", message="Withdrawal amount must be numerical values!")

    elif float(withdraw_amt) <100:
      CTkMessagebox(title="Error", message="Withdrawal amount must be higher than 100!")

    elif float(withdraw_amt) <0:
      CTkMessagebox(title="Error", message="Withdrawal amount must be greater than 0!")

    elif float(withdraw_amt) > float(amount):
      CTkMessagebox(title="Error", message="Insufficient Balance! \nDon't be a thief")

    else:
    
      try:
        con = sqlite3.connect('bank.db')
        print("1. Connection opened")

        cur = con.cursor()

        cur.execute('''UPDATE users SET amount = ?
                    WHERE username = ?''',(float(amount) - float(withdraw_amt), username))

        print("2. Update executed")


        con.commit()
        print("3. Update committed")

        cur.execute('''
                    SELECT amount FROM users
                    WHERE username = ?
                    ''', (username,))
        self.new_balance = cur.fetchone()[0]
        print("3. Update committed")

        con.close()
        print("5. Connection closed")

        msg = CTkMessagebox(title="Info", message=f"You have successfully withdrawn! \nCurrent Balance: ${self.new_balance}", icon="info")
        msg.get()
        print("6. Message box closed")

        self.back()
        print("7. Back method executed")

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