from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QComboBox, QLineEdit, QPushButton

class buyx(QDialog):
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
        
        #Buy button
        buy_button = QPushButton("Buy")
        buy_button.clicked.connect(self.execute_buy)
        layout.addWidget(buy_button)
        #placeholder for execution success and failure
        self.result_label = QLabel("")
        layout.addWidget(self.result_label)
       # self.setLayout(layout)
    def update_quote_options(self):
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
        pass
        
if __name__ == "__main__":
    app = QApplication([])
    dialog = buyx()
    dialog.show()
    app.exec_()