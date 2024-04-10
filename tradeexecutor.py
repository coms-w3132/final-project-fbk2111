from alpaca_trade_api.rest import REST, TimeFrame
Base_url = "https://paper-api.alpaca.markets"
Key_id = "PKL0F507E41ME0LEDRC1"
secret_key1 = "i3VZBPjNHSSbeFqH3a7J3c5iQdcbiUI0j5DQSVtK"
import pandas as pd

api = REST(key_id= Key_id, secret_key= secret_key1, base_url = Base_url)

bars = api.get_crypto_bars("BTC/USD", TimeFrame.Minute).df
print(bars)