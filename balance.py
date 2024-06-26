from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QPushButton
from alpaca_trade_api.rest import REST
from InputData import InputData

class Trading:
    """
    A class for interacting with trading functionalities.

    Attributes:
        api: An instance of the REST API for trading operations.

    Methods:
        __init__: Initialize the Trading class by retrieving credentials and creating an API instance.
        get_cash_balance: Retrieve the cash balance from the trading account.
        get_account_status: Retrieve the status of the trading account.

    """
    def __init__(self) -> None:
        
        base_url, key_id, secret_key = InputData.get_credentials()
        self.api = REST(key_id=key_id, secret_key=secret_key, base_url=base_url)

    def get_cash_balance(self):
        """
        Retrieve the cash balance from the trading account.

        Uses the get_account method of the REST API to retrieve account information.
        Formats the cash balance and currency as a string and returns it.

        Returns:
            str: A string representing the cash balance and currency.

        """
        account = self.api.get_account()
        cash_balance = f"{account.cash} {account.currency}"  # Concatenating cash balance and currency
        return cash_balance

    def get_account_status(self):
        """
        Retrieve the status of the trading account.

        Uses the get_account method of the REST API to retrieve account information.
        Returns the status of the trading account.

        Returns:
            str: The status of the trading account.

        """
        account = self.api.get_account()
        return account.status

class Balancex(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("My Account Balance - Alpaca")
        self.initUI()
        
    def initUI(self):
        layout = QVBoxLayout()
        see_label = QLabel("See my balance")
        self.balance_label = QLabel()  # Label to display balance
        self.buy_button = QPushButton("See Balance")
        self.buy_button.clicked.connect(self.see_balance)
        self.status = QLabel()
        layout.addWidget(see_label)
        layout.addWidget(self.buy_button)
        layout.addWidget(self.balance_label)  # Add balance label to layout
        layout.addWidget(self.status)
        self.setLayout(layout)
    
    def see_balance(self):
        trading = Trading()
        cash_balance = trading.get_cash_balance()
        self.balance_label.setText(f"Balance: {cash_balance}")
        activity = trading.get_account_status()
        self.status.setText(f"Status: {activity}")

if __name__ == "__main__":
    app = QApplication([])
    dialog = Balancex()
    dialog.show()
    app.exec_()
