import tkinter as tk
from tkinter import messagebox


class User:
    def __init__(self, name, age, gender, phone, pin):
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone
        self.pin = pin



class Bank(User):
    def __init__(self, name, age, gender, phone, pin, initial_deposit=0):
        super().__init__(name, age, gender, phone, pin)
        self.balance = initial_deposit

    def deposit(self, amount):
        self.balance += amount
        return f"Amount has been deposited: {amount}\nUpdated balance: {self.balance}"

    def withdrawal(self, amount):
        if amount > self.balance:
            return f"Insufficient Funds! Available Balance: {self.balance}"
        elif amount <= 0:
            return "You cannot withdraw a non-positive amount!"
        else:
            self.balance -= amount
            return f"Amount withdrawn: {amount}\nUpdated balance: {self.balance}"

    def show_balance(self):
        return f"Account Balance: {self.balance}"

    def transfer(self, recipient_name, amount):
        if recipient_name not in accounts:
            return "Recipient account does not exist."
        if amount > self.balance:
            return f"Insufficient Funds! Available Balance: {self.balance}"
        elif amount <= 0:
            return "You cannot transfer a non-positive amount!"
        else:
            self.balance -= amount
            accounts[recipient_name].balance += amount
            return f"Transferred {amount} to {recipient_name}. Your updated balance: {self.balance}"


# Pre-saved accounts
accounts = {
    "Mubarak": Bank("Mubarak", 30, "Male", "7041920922", "1234", initial_deposit=5000),
    "Cynthia": Bank("Cynthia", 25, "Female", "0123456789", "5678", initial_deposit=1000)
}


class BankingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Banking App")

        # Initialize current account to None
        self.current_account = None


        # Labels
        self.label = tk.Label(root, text="Hey there! Welcome to my basic python banking app what will you like to do?", font=("Arial", 14))
        self.label.pack(pady=20)

        # Buttons for login, create account, and exit
        self.login_button = tk.Button(root, text="Login", command=self.login_window, width=20)
        self.login_button.pack(pady=10)

        self.create_account_button = tk.Button(root, text="Create Account", command=self.create_account_window,
                                               width=20)
        self.create_account_button.pack(pady=10)

        self.exit_button = tk.Button(root, text="Exit", command=root.quit, width=20)
        self.exit_button.pack(pady=10)

    def login_window(self):
        login_win = tk.Toplevel(self.root)
        login_win.title("Login")

        tk.Label(login_win, text="Name:").pack(pady=5)
        name_entry = tk.Entry(login_win)
        name_entry.pack(pady=5)

        tk.Label(login_win, text="PIN:").pack(pady=5)
        pin_entry = tk.Entry(login_win, show="*")
        pin_entry.pack(pady=5)

        def login():
            name = name_entry.get()
            pin = pin_entry.get()
            if name in accounts and accounts[name].pin == pin:
                self.current_account = accounts[name]
                messagebox.showinfo("Success", f"Welcome back, {name}!")
                login_win.destroy()  # Close the login window
                self.main_menu()  # Go to main menu after login
            else:
                messagebox.showerror("Error", "Invalid name or PIN. Please try again.")

        tk.Button(login_win, text="Login", command=login).pack(pady=10)

    def create_account_window(self):
        create_win = tk.Toplevel(self.root)
        create_win.title("Create Account")

        # Input fields for account creation
        tk.Label(create_win, text="Name:").pack(pady=5)
        name_entry = tk.Entry(create_win)
        name_entry.pack(pady=5)

        tk.Label(create_win, text="Age:").pack(pady=5)
        age_entry = tk.Entry(create_win)
        age_entry.pack(pady=5)

        tk.Label(create_win, text="Gender:").pack(pady=5)
        gender_entry = tk.Entry(create_win)
        gender_entry.pack(pady=5)

        tk.Label(create_win, text="Phone:").pack(pady=5)
        phone_entry = tk.Entry(create_win)
        phone_entry.pack(pady=5)

        tk.Label(create_win, text="PIN:").pack(pady=5)
        pin_entry = tk.Entry(create_win, show="*")
        pin_entry.pack(pady=5)

        tk.Label(create_win, text="Initial Deposit:").pack(pady=5)
        deposit_entry = tk.Entry(create_win)
        deposit_entry.pack(pady=5)

        def create_account():
            name = name_entry.get()
            age = age_entry.get()
            gender = gender_entry.get()
            phone = phone_entry.get()
            pin = pin_entry.get()
            initial_deposit = float(deposit_entry.get())

            if name in accounts:
                messagebox.showerror("Error", "Account with this name already exists.")
            else:
                accounts[name] = Bank(name, age, gender, phone, pin, initial_deposit=0)
                messagebox.showinfo("Success", "Account created successfully!")
                create_win.destroy()

        tk.Button(create_win, text="Create Account", command=create_account).pack(pady=10)

    def main_menu(self):
        menu_win = tk.Toplevel(self.root)
        menu_win.title("Main Menu")

        tk.Label(menu_win, text="Main Menu", font=("Arial", 14)).pack(pady=20)

        # Display current user's details
        user_details = f"Logged in as: {self.current_account.name}\nAccount Balance: {self.current_account.balance}"
        tk.Label(menu_win, text=user_details).pack(pady=10)

        tk.Button(menu_win, text="Show Balance", command=self.show_balance).pack(pady=5)
        tk.Button(menu_win, text="Deposit", command=self.deposit_window).pack(pady=5)
        tk.Button(menu_win, text="Withdrawal", command=self.withdrawal_window).pack(pady=5)
        tk.Button(menu_win, text="Transfer", command=self.transfer_window).pack(pady=5)
        tk.Button(menu_win, text="Logout", command=lambda: self.logout(menu_win)).pack(pady=5)

    def show_balance(self):
        if self.current_account:
            balance = self.current_account.show_balance()
            messagebox.showinfo("Balance", balance)

    def deposit_window(self):
        deposit_win = tk.Toplevel(self.root)
        deposit_win.title("Deposit")

        tk.Label(deposit_win, text="Enter amount to deposit:").pack(pady=5)
        amount_entry = tk.Entry(deposit_win)
        amount_entry.pack(pady=5)

        def deposit():
            amount = float(amount_entry.get())
            result = self.current_account.deposit(amount)
            messagebox.showinfo("Deposit", result)
            deposit_win.destroy()

        tk.Button(deposit_win, text="Deposit", command=deposit).pack(pady=10)

    def withdrawal_window(self):
        withdrawal_win = tk.Toplevel(self.root)
        withdrawal_win.title("Withdrawal")

        tk.Label(withdrawal_win, text="Enter amount to withdraw:").pack(pady=5)
        amount_entry = tk.Entry(withdrawal_win)
        amount_entry.pack(pady=5)

        def withdrawal():
            amount = float(amount_entry.get())
            result = self.current_account.withdrawal(amount)
            messagebox.showinfo("Withdrawal", result)
            withdrawal_win.destroy()

        tk.Button(withdrawal_win, text="Withdraw", command=withdrawal).pack(pady=10)

    def transfer_window(self):
        transfer_win = tk.Toplevel(self.root)
        transfer_win.title("Transfer")

        tk.Label(transfer_win, text="Recipient name:").pack(pady=5)
        recipient_entry = tk.Entry(transfer_win)
        recipient_entry.pack(pady=5)

        tk.Label(transfer_win, text="Amount to transfer:").pack(pady=5)
        amount_entry = tk.Entry(transfer_win)
        amount_entry.pack(pady=5)

        def transfer():
            recipient_name = recipient_entry.get()
            amount = float(amount_entry.get())
            result = self.current_account.transfer(recipient_name, amount)
            messagebox.showinfo("Transfer", result)
            transfer_win.destroy()

        tk.Button(transfer_win, text="Transfer", command=transfer).pack(pady=10)

    def logout(self, menu_win):
        self.current_account = None  # Clear the current account
        messagebox.showinfo("Logout", "You have been logged out.")
        menu_win.destroy()  # Close the main menu and return to the main screen


# Main Application Window
root = tk.Tk()
app = BankingApp(root)
root.mainloop()
