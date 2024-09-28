from datetime import date
from datetime import datetime

class BankAccount:
    def __init__(self, owner: str, account_id: int, other_citizenship: str, city: str, balance: int, limit_minus: int):
        self.owner = owner
        self.account_id = account_id
        self.other_citizenship = other_citizenship
        self.city = city
        self.balance = balance
        self.limit_minus = limit_minus

        """
            functions:
            contractor: owner name, account id, other citizenship (if have one), city, balance, and limit minus.
            deposit: deposit money to the caller account.
            withdraw: withdraw money from the caller account.
            transfer_money: transfer money from caller account to parameter account.
        """
    def deposit(self, deposit_money: int):

        try:
            deposit_money = int(deposit_money)
            if deposit_money <= 0:
                return "Please try again a valid value greater than 0."
            self.balance += deposit_money
            return f"{self.owner} just deposited {deposit_money}, balance updated:{self.balance}."

        except ValueError:
            return "Please enter valid number."

    def withdraw(self, withdraw_money: int):
        
        try:
            withdraw_money = int(withdraw_money)
            if self.balance - withdraw_money < self.limit_minus:
                return f"You can't do this, Your current balance is:{self.balance}.\nMaximum withdraw:{self.balance - self.limit_minus}."

            elif withdraw_money <= 0:
                return "Please try again a valid value greater than 0."

            else:
                self.balance -= withdraw_money
                return f"Withdraw successfully, {self.owner} current balance is:{self.balance}"

        except ValueError:
            return "Please enter valid number."

    def transfer_money(self, account_to_transfer, transfer_money: int):

        try:
            if self.account_id == account_to_transfer.account_id:
                return "You can't transfer yourself money."

            transfer_money = int(transfer_money)
            if self.balance - transfer_money < self.limit_minus:
                return f"You can't do this, Your current balance is:{self.balance}.\nMaximum transfer:{self.balance - self.limit_minus}."

            elif transfer_money <= 0:
                return "please try again a valid value greater than 0."

            else:
                self.balance -= transfer_money
                account_to_transfer.balance += transfer_money
                return f"Transfer successfully {transfer_money} to {account_to_transfer.owner}"

        except ValueError:
            return "Please enter valid number."

    def show_account(self):
        return f"owner:[{self.owner}] || account_id:[{self.account_id}] || current_balance: [{self.balance}] || up-to-date:{date.today()} {datetime.now().strftime("%H:%M:%S")}"
