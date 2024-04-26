import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QSizePolicy, QDialog
from PyQt5.QtGui import QPixmap, QFont
from datetime import date
from cryptobuy import buyx
from cryptosell import sellx
from balance import Balancex
class BitcoinTraderApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set background image
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        background_label = QLabel()
        background_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        pixmap = QPixmap("crypto.app.icon.png")
        background_label.setPixmap(pixmap)

        # Add buttons
        self.sell_button = QPushButton("Sell", self)
        self.sell_button.clicked.connect(self.sell)
        self.sell_button.move(700, 200)  # Adjust the position as needed
        self.sell_button.setStyleSheet('color: white; background-color: orange; border: none; border-radius: 10px; padding: 10px; font-family: cursive; font-size: 15px;')
        self.sell_button.setParent(background_label)

        self.buy_button = QPushButton("Buy", self)
        self.buy_button.clicked.connect(self.buy)
        self.buy_button.move(700, 300)  # Adjust the position as needed
        self.buy_button.setStyleSheet('color: white; background-color: purple; border: none; border-radius: 10px; padding: 10px; font-family: cursive; font-size: 15px;')
        self.buy_button.setParent(background_label)

        self.balance_button = QPushButton("See Balance", self)
        self.balance_button.clicked.connect(self.see_balance)
        self.balance_button.move(700, 400)  # Adjust the position as needed
        self.balance_button.setStyleSheet('color: white; background-color: red; border: none; border-radius: 10px; padding: 10px; font-family: cursive; font-size: 15px;')
        self.balance_button.setParent(background_label)

        self.strategy_button = QPushButton("Trading Strategy", self)
        self.strategy_button.clicked.connect(self.trading_strategy)
        self.strategy_button.move(700, 500)  # Adjust the position as needed
        self.strategy_button.setStyleSheet('color: white; background-color: blue; border: none; border-radius: 10px; padding: 10px; font-family: cursive; font-size: 15px;')
        self.strategy_button.setParent(background_label)
        
        self.record_button = QPushButton("Records", self)
        self.record_button.clicked.connect(self.records)
        self.record_button.move(700, 600)  # Adjust the position as needed
        self.record_button.setStyleSheet('color: white; background-color: green; border: none; border-radius: 10px; padding: 10px; font-family: cursive; font-size: 15px;')
        self.record_button.setParent(background_label)
        
        self.record = QLabel("Designed by Filimon Mackenzie Keleta. All right reserved", self)
        self.record.setGeometry(650, 800, 380, 50)
        self.record.setStyleSheet('font-size: 12px; color: black;')

        

        layout.addWidget(background_label)
        central_widget.setLayout(layout)

        # Set window title and size
        self.setWindowTitle("Alpaca Crypto Trading Bot")
        self.resize(800, 600)
        # Setting header and size for the app
        title_label = QLabel("Crypto Trading Strategy", self)
        title_label.setGeometry(600, 150, 380, 50)
        title_label.setStyleSheet('font-size: 30px; font-weight: bold; color: violet;')

    def buy(self):
        #app = QApplication([])
        dialog = buyx()
        dialog.exec()
         
    def sell(self):
        #app = QApplication([])
        dialog = sellx()
        dialog.exec()

    def see_balance(self):
        dialog = Balancex()
        dialog.exec()

    def trading_strategy(self):
        pass
    def records(self):
        pass
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BitcoinTraderApp()
    window.show()
    sys.exit(app.exec_())
