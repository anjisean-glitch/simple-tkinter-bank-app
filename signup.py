#Create a simple banking application 
# The application should be able to allow the user to create an account, 

import customtkinter as ctk
import subprocess
import sqlite3
import dbconnect
from CTkMessagebox import CTkMessagebox

class Bank:
  def __init__(self):
    self.root = ctk.CTk()
    self.root.title("Signup Page")
    self.root.geometry("700x600+0+0")
    self.root.configure(fg_color="#130475")

    ## title 
    self.title_lbl = ctk.CTkLabel(self.root, text="SIGNUP PAGE", font=("Arial", 35, "bold"), fg_color="#130475", text_color="white", underline=0)
    self.title_lbl.pack(padx=5, pady=10)
    ########

    ## sub text
    self.text_lbl = ctk.CTkLabel(self.root, text="Let's set up your account!!", font=("Arial", 20, "bold"), fg_color="#130475", text_color="white", underline=5)
    self.text_lbl.pack(padx=5, pady=10)
    ############
    
    
    ## Frame for the inputs ###################################################
    self.frm1 = ctk.CTkFrame(self.root, fg_color="#130475")

    ## input 1, the Username label
    self.input1_lbl = ctk.CTkLabel(self.frm1, text="Enter username: ", fg_color="#130475", text_color="white", font=("Arial", 25))
    self.input1_lbl.grid(row=0, column=0, padx=10, pady=10)

    ## input 1, the Username entry
    self.input1_ent = ctk.CTkEntry(self.frm1, fg_color="white", text_color="black", font=("Arial", 25), width=300)
    self.input1_ent.grid(row=0, column=1, padx=10, pady=10)

    ## input 2, the email label
    self.input2_lbl = ctk.CTkLabel(self.frm1, text="Enter email: ", fg_color="#130475", text_color="white", font=("Arial", 25))
    self.input2_lbl.grid(row=1, column=0, padx=10, pady=10)

    ## input 2, the email entry
    self.input2_ent = ctk.CTkEntry(self.frm1, fg_color="white", text_color="black", font=("Arial", 25), width=300)
    self.input2_ent.grid(row=1, column=1, padx=10, pady=10)
    
    ## input 3, the 4-digit pin label
    self.input3_lbl = ctk.CTkLabel(self.frm1, text="Enter 4 digit pin: ", fg_color="#130475", text_color="white", font=("Arial", 25))
    self.input3_lbl.grid(row=2, column=0, padx=10, pady=20)

    ## input 3, the 4-digit pin entry
    self.input3_ent = ctk.CTkEntry(self.frm1, fg_color="white", text_color="black", font=("Arial", 25), width=100)
    self.input3_ent.grid(row=2, column=1, padx=10, pady=20)

    self.frm1.pack(padx=10, pady=10)
    #############################################################################


    ## Signup button
    self.signup_btn = ctk.CTkButton(self.root, text="Signup", fg_color="white", text_color="black", hover_color="green", font=("Arial", 30), command = self.signup)
    self.signup_btn.pack(padx=10, pady=30)

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

  def signup(self):
    username = self.input1_ent.get().strip()
    email = self.input2_ent.get().strip()
    pin = self.input3_ent.get().strip()

    if not pin or not email or not username:
      CTkMessagebox(title="Error", message="Enter all inputs to sign up")

    elif not pin.isdigit():
      CTkMessagebox(title="Error", message="Pin must be numerical values")

    elif len(pin) != 4:
      CTkMessagebox(title="Error", message="Pin length must be 4")

    else:
      con=sqlite3.connect('bank.db')
      cur=con.cursor()

      cur.execute('''INSERT INTO users(username,email,pin)
                      VALUES(?,?,?)''',(username,email,pin))
      # for record to show in the table of database you commit

      
      con.commit()
      con.close()

      CTkMessagebox(title="Information", message="You have successfully signed up")

      self.input1_ent.delete(0, "end")
      self.input2_ent.delete(0, "end")
      self.input3_ent.delete(0, "end")



Bank()
