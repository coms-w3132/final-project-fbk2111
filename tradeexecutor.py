from alpaca_trade_api.rest import REST, TimeFrame
import io
import pandas as pd
import InputData 
import alpaca_trade_api
help('alpaca_trade_api.rest')
class Trading:
    def __init__(self) -> None:
        self.api = REST(key_id= InputData.Key_id, secret_key= InputData.secret_key1, base_url = InputData.Base_url)

    timeframe = TimeFrame.Minute
    symbol = "BTC/USD"
    
    '''
    # I can get historical data for a given period of time with this 
    def get_crypto_bars(self, symbol, timeframe, start, end, limit, sort, loc):
        bars = self.api.get_crypto_bars(symbol, TimeFrame.timeframe).df
    # to create a market order to buy any cryptocoin
    def marketbuy(self):
        purchase = self.api.submit_order('symbol', qty=1, side='buy')
    def marketsell(self):
        purchase = self.api.submit_order('symbol', qty=1, side='sell')
    #cancels all open order
    def cancel_all_orders(self):
        purchase = self.api.cancel_all_orders()
    #to see current open order
    def open_order_list(self):
       purchase =  api.cancel_all_orders()
    #to cancel specific order, symbol required
    def cancel_order(Self, symbol):
        purchase = api.cancel_order(symbol)
    
    #self.api.get_all_positions()
    def add_to_watchlist(self, symbol):
       purchase = api.add_to_watchlist(symbol=symbol)
       
'''    
close_all_positions
close_position
create_watchlist
data_get
delete
delete_watchlist
get
get_account
get_account_configurations
get_activities
get_assest
get_crypto_bars
get_crypto_bars_iter
get_crypto_quotes
get_crypto_quotes_iter
get_crypto_snapshots
get_crypto_trade
get_crypto_trades_iter
get_latest_bar
get_latest_crypto_bar
get_latest_crypto_orderbooks
get_latest_quote
get_latest_quotes
get_latest_trade
get_latest_trades
get_order
get_portfolio_history
get_position
get_trades
get_watchlists
list_orders
put
replace_order
submit_order
update_account_configurations
update_watchlist

