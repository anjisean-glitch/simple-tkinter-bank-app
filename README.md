# Simple Tkinter Bank App

A desktop banking application built with Python, CustomTkinter and SQLite. This project simulates basic banking operations through a graphical user interface.

## Features

- User account registration
- User sign-in using username or email and a four-digit PIN
- Account dashboard displaying the user's balance
- Deposit funds
- Withdraw funds
- Transfer funds to another registered user
- SQLite database integration

## Technologies Used

- Python
- CustomTkinter
- SQLite3
- CTkMessagebox
- Subprocess and command-line arguments

## Project Structure

| File | Purpose |
|---|---|
| `main.py` | Main account dashboard |
| `signup.py` | Account registration |
| `signin.py` | User authentication |
| `deposit.py` | Deposit operations |
| `withdraw.py` | Withdrawal operations |
| `transfer.py` | Fund transfers |
| `dbconnect.py` | Database and table creation |

## Installation

1. Install Python.
2. Clone this repository:

   `git clone https://github.com/anjisean-glitch/simple-tkinter-bank-app.git`

3. Navigate into the project folder:

   `cd simple-tkinter-bank-app`

4. Install the required packages:

   `pip install customtkinter CTkMessagebox`

## Running the Application

Start the sign-in page:

`python signin.py`

You can create a new account through the signup option.

The application creates its local SQLite database when it runs.

## What I Learned

Through this project, I practised:

- Building graphical user interfaces with CustomTkinter.
- Organising Python applications using classes and methods.
- Connecting Python applications to SQLite databases.
- Performing database operations using SQL.
- Passing information between Python scripts using `subprocess` and `sys.argv`.
- Implementing basic input validation and transaction logic.

## Important Note

This is an educational project created for learning and practice. It is not production-ready banking software.

It does not implement secure PIN hashing or production-grade financial security.

---

**Developed by Anji**

Analyze with Anji — Understand. Analyze. Build.
