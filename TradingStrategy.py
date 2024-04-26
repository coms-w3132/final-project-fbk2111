'''from alpaca_trade_api.rest import REST, TimeFrame
import pandas as pd
import matplotlib.pylot as plt
import numpy as np
import math



class strategy:
    def __init__(self) -> None:
        self.api = REST(key_id= InputData.Key_id, secret_key= InputData.secret_key1, base_url = InputData.Base_url)
        
        
'''
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QSizePolicy
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create a central widget to hold the QLabel
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Create a QVBoxLayout to arrange widgets vertically
        layout = QVBoxLayout(central_widget)

        # Initialize the QLabel
        background_label = QLabel()

        # Set the size policy of the QLabel to expand and fill the available space
        background_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Load the original QPixmap
        pixmap = QPixmap("crypto.app.icon.png")

        # Set the scaled pixmap to the QLabel
        background_label.setPixmap(pixmap)

        # Add the QLabel to the layout
        layout.addWidget(background_label)

        # Set the layout for the central widget
        central_widget.setLayout(layout)

        # Set window title and size
        self.setWindowTitle("Crypto App")
        self.resize(800, 600)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
