from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QComboBox, QLineEdit, QPushButton, QGraphicsView, QGraphicsScene
from alpaca_trade_api.rest import REST, TimeFrame
import pandas as pd
from collections import deque
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from InputData import InputData
import datetime
class Trading:
    def api(self) -> REST:
        base_url, key_id, secret_key = InputData.get_credentials()
        api = REST(key_id=key_id, secret_key=secret_key, base_url=base_url)
        return api

class buyx(QDialog):
    """
    Initialize the Crypto BUY Alpaca application window.

    Sets the window title and initializes the UI elements.

    Args:
        parent: Optional parent widget.

    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Crypto Purchase Alpaca")
        self.initUI()
        
        
    def initUI(self):
        layout = QVBoxLayout()
        base_label = QLabel("Base Bitcoin:")
        self.base_combo = QComboBox()
        self.base_combo.addItem("BTC")
        self.base_combo.addItem("USDT")
        self.base_combo.addItem("USDC")
        self.base_combo.addItem("USD")
        self.base_combo.currentTextChanged.connect(self.update_quote_options)
        layout.addWidget(base_label)
        layout.addWidget(self.base_combo)
        # Quote Bitcoin Selection
        quote_label = QLabel("Quote Bitcoin:")
        self.quote_combo = QComboBox()
        self.update_quote_options()
        layout.addWidget(quote_label)
        layout.addWidget(self.quote_combo)
        
        #amout input
        amount_label = QLabel("Amount:")
        self.amount_edit = QLineEdit()
        layout.addWidget(amount_label)
        layout.addWidget(self.amount_edit)
        note = QLabel("Please do not buy more than 0.1 Bitcoin or less than 0.001, only Engage in BTC and ETH Trade for This account")
        layout.addWidget(note)
        #Buy button
        buy_button = QPushButton("Buy")
        buy_button.clicked.connect(self.execute_buy)
        layout.addWidget(buy_button)
        #placeholder for execution success and failure
        self.result_label = QLabel("")
        layout.addWidget(self.result_label)
        self.balance_label = QLabel("")
        layout.addWidget(self.balance_label)
        self.plot_view = QGraphicsView()
        layout.addWidget(self.plot_view)
        self.setLayout(layout)
    def update_quote_options(self):
        """
        Update the options available for selecting a quote currency based on the selected base currency.

        Retrieves the currently selected base currency from the base_combo widget and updates the available
        options in the quote_combo widget accordingly.

        Available quote options are stored in a dictionary where the keys represent base currencies and the values
        are lists of corresponding quote currencies.

        Example:
        If "BTC" is selected as the base currency, the available quote currencies will be ["BCH", "ETH", "LTC", "UNI"].

        """
        base = self.base_combo.currentText()
        quotes = {
            "BTC": ["BCH", "ETH", "LTC", "UNI"],
            "USDT": ["AAVE", "BCH", "BTC", "ETH", "LINK", "LTC", "UNI"],
            "USDC": ["AAVE", "AVAX", "BAT", "BCH", "BTC", "CRV", "DOT", "ETH", "GRT", "LINK", "LTC", "MKR", "SHIB", "UNI", "XTZ"],
            "USD": ["AAVE", "AVAX", "BAT", "BCH", "BTC", "CRV", "DOT", "ETH", "GRT", "LINK", "LTC", "MKR", "SHIB", "UNI", "USDC", "USDT", "XTZ"]
        }
        self.quote_combo.clear()
        self.quote_combo.addItems(quotes.get(base, []))
    def execute_buy(self):
        """
        Execute a buy order based on the selected base currency.

        If the base currency is "BTC", the purchase quote will be set to "BTC/USD", otherwise "ETH/USD" will be used.
        Retrieves the amount to buy from the amount_edit widget.
        Defines a start and end date for retrieving historical data.
        Retrieves historical price data for the chosen purchase quote.
        Calculates short and long moving averages.
        Executes a buy order if the amount to buy is greater than 0.5 and the short moving average is greater than the long moving average.
        Updates UI labels with transaction information and plots the price of the chosen cryptocurrency over time.
        Logs transaction details to a text file.

        """
        purchase_quotes = None
        if self.base_combo.currentText() == "BTC":
            purchase_quotes = "BTC"
        else:
            purchase_quotes = "ETH"
        purchase_quote = purchase_quotes + "/USD"
        amount = float(self.amount_edit.text())
        star_date = "2023-05-08"
        end_date = "2024-05-08"
        currency  = Trading()
        api = currency.api()
        time_in_forces = 'gtc'
        bars = api.get_crypto_bars(purchase_quote, TimeFrame.Day , start=star_date, end= end_date).df
        # defining moving averages
        short_window = 20 
        long_window = 50
        if amount > 0.5:
            return 0
        bars['Short_MA'] = bars['close'].rolling(window=short_window, min_periods=1).mean()
        bars['Long_MA'] = bars['close'].rolling(window=long_window, min_periods=1).mean()
        # Two queue to have the values of the moving average
        
        short_maqueue = deque(maxlen=long_window)
        long_maqueue = deque(maxlen=long_window)
        
        account = api.get_account()
        cash_balance = account.cash # Concatenating cash balance and currency

        for index, row, in bars.iterrows():
            short_maqueue.append(row["Short_MA"])
            long_maqueue.append(row["Long_MA"])
            
            if len(short_maqueue) == long_window:
                short_maqueue_avg = sum(short_maqueue) / long_window
                long_maqueue_avg = sum(long_maqueue) / long_window
                
                if short_maqueue_avg > long_maqueue_avg:
                    # if the short moving aveage is greater than long moving average we buy
                    buy = api.submit_order(purchase_quote, qty=amount, side='buy', time_in_force=time_in_forces)
                    if buy is not None:   
                        self.result_label.setText(f'you have bought {amount} of {purchase_quotes}. Congrats.')
                        cash_balance = api.get_account().cash
                        cash_balance = str(cash_balance)
                        self.balance_label.setText(f'Balance: {cash_balance}')
                        fig, ax = plt.subplots()
                        ax.plot(bars.index, bars['close'], label='Price')
                        ax.set_xlabel('Date')
                        ax.set_ylabel('Price ($)')
                        ax.set_title(f'Price of {purchase_quote} Over Time')
                        ax.legend()
                        plt.close(fig)
                        canvas = FigureCanvas(fig)
                        scene = QGraphicsScene()
                        scene.addWidget(canvas)
                        
                        self.plot_view.setScene(scene)
                        current_date_time = datetime.datetime.now()
                        f = open("transaction.txt", "a")
                        f.write(f'Log Entry Time: {current_date_time}\n')
                        f.write(f'You have bought {amount} amount of {purchase_quotes} coin. Congrats.\n')
                        f.write(f'Balance: {cash_balance}\n')
                        f.close()
                            
                            
                            
                        
                    else:
                        self.result_label.setText("Insufficient Funds")
                        print("no money")
                    return 
        
if __name__ == "__main__":
    app = QApplication([])
    dialog = buyx()
    dialog.show()
    app.exec_()