from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QPushButton, QComboBox, QTextBrowser
from alpaca_trade_api.rest import REST, TimeFrame
from InputData import InputData
import pandas as pd

class Trading:
    
    def __init__(self) -> None:
        base_url, key_id, secret_key = InputData.get_credentials()
        self.api = REST(key_id=key_id, secret_key=secret_key, base_url=base_url)

        
    def get_crypto_bars(self, symbol, timeframe):
        """
    Fetch cryptocurrency bars and statistics for a given symbol and timeframe.

    Calls the get_crypto_bars method of the API instance with the specified symbol and timeframe.
    Returns the DataFrame containing the fetched bars and statistics.

    Args:
        symbol: The cryptocurrency symbol to fetch bars for.
        timeframe: The timeframe for the bars (e.g., TimeFrame.Minute, TimeFrame.Hour).

    Returns:
        pandas DataFrame: A DataFrame containing the fetched bars and statistics.

        """
        bars = self.api.get_crypto_bars(symbol, timeframe).df #fetch crypto bars and stats 
        return bars


class records(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Crypto Daily Record Alpaca")
        self.initUI()
        
        
    def initUI(self):
        layout = QVBoxLayout()
        base_label = QLabel("Base Bitcoin:")
        self.base_combo = QComboBox()
        self.base_combo.addItem("Bitcoin to US Dollar (BTC/USD)")
        self.base_combo.addItem("Ethereum to US Dollar (ETH/USD)")
        self.base_combo.addItem("Litecoin to US Dollar (LTC/USD)")
        self.base_combo.addItem("Bitcoin Cash to US Dollar (BCH/USD)")
        self.base_combo.addItem("Chainlink to US Dollar (LINK/USD)")
        self.base_combo.addItem("Ripple to US Dollar (XRP/USD)")
        self.base_combo.addItem("Cardano to US Dollar (ADA/USD)")
        self.base_combo.addItem("Dogecoin to US Dollar (DOGE/USD)")
        self.base_combo.addItem("Polkadot to US Dollar (DOT/USD)")
        self.base_combo.addItem("Uniswap to US Dollar (UNI/USD)")
        self.base_combo.currentTextChanged.connect(self.update_quote_options)
        layout.addWidget(base_label)
        layout.addWidget(self.base_combo)
        # Quote Bitcoin Selection
        quote_label = QLabel("TimeFrame")
        self.quote_combo = QComboBox()
        self.update_quote_options()
        layout.addWidget(quote_label)
        layout.addWidget(self.quote_combo)
        
        #Get Record buttion 
        record_button = QPushButton("Get Record")
        record_button.clicked.connect(self.execute_record)
        layout.addWidget(record_button)
        #placeholder for execution success and failure
        self.result_box = QTextBrowser()
        layout.addWidget(self.result_box)
        self.setLayout(layout)
    def update_quote_options(self):
        base = self.base_combo.currentText()
        quotes = {
            "Bitcoin to US Dollar (BTC/USD)": ["Minute", "Hour"],
            "Ethereum to US Dollar (ETH/USD)": ["Minute", "Hour"],
            "Litecoin to US Dollar (LTC/USD)": ["Minute", "Hour"],
            "Bitcoin Cash to US Dollar (BCH/USD)": ["Minute", "Hour"],
            "Chainlink to US Dollar (LINK/USD)": ["Minute", "Hour"],
            "Ripple to US Dollar (XRP/USD)": ["Minute", "Hour"],
            "Cardano to US Dollar (ADA/USD)": ["Minute", "Hour"],
            "Polkadot to US Dollar (DOT/USD)": ["Minute", "Hour"],
            "Dogecoin to US Dollar (DOGE/USD)": ["Minute", "Hour"],
            "Uniswap to US Dollar (UNI/USD)": ["Minute", "Hour"],
             
        }
        self.quote_combo.clear()
        self.quote_combo.addItems(quotes.get(base, []))
    def execute_record(self):
        """
    Display market data in HTML format based on the selected base currency and timeframe.

    Creates an instance of the Trading class.
    Extracts the base currency from the selected base_combo text.
    Gets the selected timeframe from the quote_combo.
    Calls the get_crypto_bars method of the Trading instance based on the selected base currency and timeframe.
    If market data is available, converts it to HTML format and sets it in the result_box widget.
    If no market data is available, displays a message indicating that the trading exchange platform is working on it.

        """
        trading = Trading()
        base_text = self.base_combo.currentText()
        base = base_text.split()[-1]  # Extracting the symbol and currency pair
        
        base_currency = base[1:len(base) - 1]  # Extracting the base currency
        print(base_currency)
        quore = "" + base_currency
        timeframe = self.quote_combo.currentText()  # Getting the selected timeframe
        if timeframe == "Minute":
            bars = trading.get_crypto_bars(quore, TimeFrame.Minute)
            
        if timeframe == "Hour":
            bars = trading.get_crypto_bars(quore, TimeFrame.Hour)
        if bars is not None:
            bars_html = bars.to_html()
            self.result_box.setHtml(bars_html)
        else:
            
            self.result_box.setText("No Market Data Available. Trading exchange platform working on it - _ -")
            
        
if __name__ == "__main__":
    app = QApplication([])
    dialog = records()
    dialog.show()
    app.exec_()
    
