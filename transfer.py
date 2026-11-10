#Create a simple banking application 
# The application should be able to allow the user to create an account, 

import customtkinter as ctk
import subprocess
import sqlite3
from CTkMessagebox import CTkMessagebox
import dbconnect
import sys

## variables gotten from the subprocess Popen code inside the transfer function inside the main.py
username = sys.argv[1]
email = sys.argv[2]
pin = sys.argv[3]
amount = sys.argv[4]
######################################################################

class Bank:
  def __init__(self):
    self.root = ctk.CTk()
    self.root.title(f"Transfer Page/{username}")
    self.root.geometry("900x600+0+0")
    self.root.configure(fg_color="#130475")

    ## Title#######
    self.title = ctk.CTkLabel(self.root, text="WELCOME TO THE TRANSFER PAGE", font=("Arial", 40, "bold"), fg_color="#130475", text_color="white", underline=0)
    self.title.pack(padx=10, pady=20)
    ###############


    ## frame 1 for the transfer amount
    self.frm1 = ctk.CTkFrame(self.root, fg_color="#130475")

    self.que_lbl = ctk.CTkLabel(self.frm1, text="How much would you like to transfer: ", font=("Arial", 25), fg_color="#130475", text_color="white")
    self.que_lbl.grid(row=0, column=0)

    self.transfer_amt = ctk.CTkEntry(self.frm1, font=("Arial", 25), fg_color="white", text_color="black")
    self.transfer_amt.grid(row=0, column=1)

    self.frm1.pack(padx=10, pady=30)
    ##################################


    ## frame 2 for the receivers account
    self.frm2 = ctk.CTkFrame(self.root, fg_color="#130475")

    self.receiver_acc_lbl = ctk.CTkLabel(self.frm2, text="Who do you wish to transfer to:\n Please Enter either their username or account name ", font=("Arial", 25), fg_color="#130475", text_color="white")
    self.receiver_acc_lbl.grid(row=1, column=0)

    self.receiver_acc_ent = ctk.CTkEntry(self.frm2, font=("Arial", 25), fg_color="white", text_color="black", width=250)
    self.receiver_acc_ent.grid(row=1, column=1)
    

    self.frm2.pack(padx=10, pady=30)
    #####################################

    ## transfer btn ######################
    self.transfer_btn = ctk.CTkButton(self.root, text="TRANSFER", font=("Arial", 30), fg_color="black", text_color="white", hover_color="green", command=self.transfer)
    self.transfer_btn.pack(padx=10, pady=20)
    ######################################

    ## back to main label
    self.main_lbl = ctk.CTkLabel(self.root, text="Go Back To Main Page?", font=("Arial", 25), fg_color="#130475", text_color="white")
    self.main_lbl.pack(padx=10, pady=(50, 0))
    
    ## back to main button
    self.main_pg = ctk.CTkButton(self.root, text="Back", fg_color="black", text_color="white", hover_color="green", font=("Arial", 18), command = self.back)
    self.main_pg.pack(padx=10)

    ## credit
    self.credit = ctk.CTkLabel(self.root, text="MADE BY ANJI", fg_color="#130475", text_color="dark grey", font=("Arial", 15))
    self.credit.pack(padx=10, pady=50)

    self.root.mainloop()

  ## transfer function ########################
  def transfer(self):
    transfer_amt = self.transfer_amt.get().strip()
    receiver = self.receiver_acc_ent.get().strip()

    if not transfer_amt and not receiver:
      CTkMessagebox(title="Error", message="Please fill all the space")

    elif not transfer_amt.isdigit():
      CTkMessagebox(title="Error", message="Transfer amount must be numerical values!")

    elif float(transfer_amt) <100:
      CTkMessagebox(title="Error", message="Transfer amount must be higher than 100!")
    
    elif float(transfer_amt) > float(amount):
      CTkMessagebox(title="Error", message="Insufficient Balance! \nYou can't make this transaction")

    else:
      try:
        con = sqlite3.connect('bank.db')
        cur = con.cursor()

        cur.execute("""SELECT * 
                    FROM users
                    WHERE username LIKE ?
                    OR email LIKE ?""",
                    (receiver,receiver))
        con.commit()
       


        result = cur.fetchone()
        receiver_og_amount = result[4]  

       

        if result:
          try:
            con = sqlite3.connect('bank.db')
            print("Connection created")
            
            cur = con.cursor()
            print("Cursor created")
            


            cur.execute('''UPDATE users SET amount = ?
                        WHERE username = ?''',(float(amount) - float(transfer_amt), username))
            print("DEDUCTION successful")

            con.commit()
            print(" COMMIT OF DEDUCT successful")

            cur.execute('''UPDATE users SET amount = ?
                        WHERE username = ?
                        or email = ?''',(float(receiver_og_amount) + float(transfer_amt), receiver, receiver))


            con.commit()

            cur.execute("""SELECT * 
                        FROM users
                        WHERE username LIKE ?
                        OR email LIKE ?""",
                        (username,email))
            con.commit()
            

            self.new_balance = cur.fetchone()[4]
            con.close()
            print("Balance retrieved")

            msg = CTkMessagebox(title="Info", message=f"You have successfully transferred ${transfer_amt} to {receiver}! \nCurrent Balance: ${self.new_balance}", icon="info")
            msg.get()
    
            self.back()

          except Exception as e:
            CTkMessagebox(title="Error", message=str(e))

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