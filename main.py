#Create a simple banking application 
# The application should be able to allow the user to create an account, 

import customtkinter as ctk
import subprocess
import sqlite3
from CTkMessagebox import CTkMessagebox
import dbconnect
import sys


## variables gotten from the subprocess Popen code inside the signin function inside the signin.py
username = sys.argv[1]
email = sys.argv[2]
pin = sys.argv[3]
amount = sys.argv[4]
##################################################################################################

class Bank:
  def __init__(self):
    self.root = ctk.CTk()
    self.root.title(f"Main Page/{username}")
    self.root.geometry("700x600+0+0")
    self.root.configure(fg_color="#130475")

    ## title ###################
    self.title = ctk.CTkLabel(self.root, text=f"GREETINGS {username}", font=("Arial", 40, "bold"), fg_color="#130475", text_color="white", underline=0)
    self.title.pack()
    ############################

    ## to display the user's account balance ##################
    self.amount_lbl = ctk.CTkLabel(self.root, text=f"BALANCE: ${amount}", font=("Arial", 35), fg_color="#130475", text_color="white")
    self.amount_lbl.pack(padx=20, pady=20)
    ###########################################################

    ## Label asking user what they wish to do #########
    self.que_lbl = ctk.CTkLabel(self.root, text="What do you wish to do: ", font=("Arial", 35), fg_color="#130475", text_color="white")
    self.que_lbl.pack(padx=20, pady=(20,15))
    ###################################################


    ## frame to hold the buttons for the options they have
    self.options_frm = ctk.CTkFrame(self.root, fg_color="#130475")

    ## deposit button #########
    self.deposit_btn = ctk.CTkButton(self.options_frm, text="Deposit", font=("Arial", 30), fg_color="black", text_color="white", hover_color="green", command=self.deposit)
    self.deposit_btn.grid(row=0, column=0)

    ## withdraw button #########
    self.withdraw_btn = ctk.CTkButton(self.options_frm, text="Withdraw", font=("Arial", 30), fg_color="black", text_color="white", hover_color="green", command=self.withdraw)
    self.withdraw_btn.grid(row=1, column=0)

    ## transfer button #########
    self.transfer_btn = ctk.CTkButton(self.options_frm, text="Transfer", font=("Arial", 30), fg_color="black", text_color="white", hover_color="green", command=self.transfer)
    self.transfer_btn.grid(row=2, column=0)

    self.exit_btn = ctk.CTkButton(self.options_frm, text="Exit", font=("Arial", 30), fg_color="black", text_color="white", hover_color="green", command=self.exit)
    self.exit_btn.grid(row=3, column=0)

    self.options_frm.pack(padx=10, pady=20)

     ## signin option label
    self.signin_lbl = ctk.CTkLabel(self.root, text="Go Back To Sign-in Page?", font=("Arial", 25), fg_color="#130475", text_color="white")
    self.signin_lbl.pack(padx=10, pady=(50, 0))
    
    ## signin option button
    self.signin_pg = ctk.CTkButton(self.root, text="Signin", fg_color="black", text_color="white", hover_color="green", font=("Arial", 18), command = self.signin)
    self.signin_pg.pack(padx=10)
    
    


    ## credit
    self.credit = ctk.CTkLabel(self.root, text="MADE BY ANJI", fg_color="#130475", text_color="dark grey", font=("Arial", 15))
    self.credit.pack(padx=10, pady=50)

    self.root.mainloop()


  ## function to return to signin page ################
  def signin(self):
    subprocess.Popen(["python","signin.py"])
    self.root.destroy()
  #####################################################

  ## deposit function ###############
  def deposit(self):
    try:
      subprocess.Popen([
      "python",
      "deposit.py",
      username,
      email,
      pin,
      amount
  ])

      self.root.destroy()

    except Exception as e:
      CTkMessagebox(title="Error", message=str(e))


  ## withdraw function ###############
  def withdraw(self):
    try:
      subprocess.Popen([
      "python",
      "withdraw.py",
      username,
      email,
      pin,
      amount
  ])

      self.root.destroy()

    except Exception as e:
      CTkMessagebox(title="Error", message=str(e))
    
  ## transfer function ###############
  def transfer(self):
    try:
      subprocess.Popen([
      "python",
      "transfer.py",
      username,
      email,
      pin,
      amount
  ])

      self.root.destroy()

    except Exception as e:
      CTkMessagebox(title="Error", message=str(e))

  ## exit function ###############
  def exit(self):
    self.root.destroy()

Bank()

