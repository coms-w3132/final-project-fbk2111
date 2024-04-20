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
    #Liquidates all open positions at market price    
    def close_all_positions():
        purchase = api.close_all_positions():
    def close_position(self,symbol, qty, float=None):
        purchase = api.close_position(symbol, qty, float=None):
    def watchlist(self, watchlistid):
        purchase = api.delete_watchlist(watchlistid)
    def get_account(self):
        purchase = api.get_account(self)
    def get_crypto_bars(self, symbol: Union[str, List[str]], timeframe: alpaca_trade_api.rest.TimeFrame, start: Optional[str] = None, end: Optional[str] = None, limit: int = None, sort: Optional[alpaca_trade_api.rest.Sort] = None, loc: str = 'us'):
        purchase = api.get_crypto_bars()
    def crypto_bars_iter(self, symbol: Union[str, List[str]], timeframe: alpaca_trade_api.rest.TimeFrame, start: Optional[str] = None, end: Optional[str] = None, limit: int = None, sort: Optional[alpaca_trade_api.rest.Sort] = None, loc: str = 'us', raw=False):
        purchase = api.cypto_bars_iter()
    def crypto_quotes(self, symbol: Union[str, List[str]], start: Optional[str] = None, end: Optional[str] = None, limit: int = None, sort: Optional[alpaca_trade_api.rest.Sort] = None, loc: str = 'us', raw=False):
        purchase = api.crypto_quotes(self, symbol: Union[str, List[str]], start: Optional[str] = None, end: Optional[str] = None, limit: int = None, sort: Optional[alpaca_trade_api.rest.Sort] = None, loc: str = 'us', raw=False)
    def get_crypto_trade(self, symbol: Union[str, List[str]], start: Optional[str] = None, end: Optional[str] = None, limit: int = None, sort: Optional[alpaca_trade_api.rest.Sort] = None, loc: str = 'us'):
        purchase = api.get_crypto_trade(self, symbol: Union[str, List[str]], start: Optional[str] = None, end: Optional[str] = None, limit: int = None, sort: Optional[alpaca_trade_api.rest.Sort] = None, loc: str = 'us')
    def get_latest_crypto_bar(self, symbol: str, feed: Optional[str] = None):
        purhcase = api.get_latest_bar(self, symbol: str, feed: Optional;[str] = None)
    def get_latest_crypto_orderbook(self, symbol: str, loc: str = 'us'):
        purchase = api.get_latest_crypto_orderbook(self, symbol: str, loc: str = 'us')
    def get_latest_crypto_quotes(self, symbols: List[str], loc: str = 'us'):
        purchase = api.get_latest_crypto_quotes(self, symbols: List[str], loc: str = 'us')
    def get_latest_quotes(self, symbols: List[str], feed: Optional[str] = None):
        purchase = api.get_latest_quotes(self, symbols: List[str], feed: Optional[str] = None)
    def  get_latest_trades(self, symbols: List[str], feed: Optional[str] = None):
        purchase = api. get_latest_trades(self, symbols: List[str], feed: Optional[str] = None)
    def get_order(self, order_id: str, nested: bool = None):
        purhcase = api.get_order(self, order_id: str, nested: bool = None)
    def get_portfolio_history(self, date_start: str = None, date_end: str = None, period: str = None, timeframe=None, extended_hours: bool = None) :
        purhcase = api.et_portfolio_history(self, date_start: str = None, date_end: str = None, period: str = None, timeframe=None, extended_hours: bool = None) 
    def get_position(self, symbol: str):
        purchase = api.get_position(self, symbol: str)
    def get_trades_iter(self, symbol: Union[str, List[str]], start: Optional[str] = None, end: Optional[str] = None, limit: int = None, feed: Optional[str] = None, asof: Optional[str] = None, sort: Optional[
alpaca_trade_api.rest.Sort] = None, raw=False):
        purchase = api.get_trades_iter(self, symbol: Union[str, List[str]], start: Optional[str] = None, end: Optional[str] = None, limit: int = None, feed: Optional[str] = None, asof: Optional[str] = None, sort: Optional[
alpaca_trade_api.rest.Sort] = None, raw=False)
    def list_orders(self, status: str = None, limit: int = None, after: str = None, until: str = None, direction: str = None, params=None, nested: bool = None, symbols: List[str] = None, side: str = None):
        purhcase = api.list_orders(self, status: str = None, limit: int = None, after: str = None, until: str = None, direction: str = None, params=None, nested: bool = None, symbols: List[str] = None, side: str = None)
    def replace_order(self, order_id: str, qty: str = None, limit_price: str = None, stop_price: str = None, trail: str = None, time_in_force: str = None, client_order_id: str = None):
        purhcase = api.replace_order(self, order_id: str, qty: str = None, limit_price: str = None, stop_price: str = None, trail: str = None, time_in_force: str = None, client_order_id: str = None)   
    def update_watchlist(self, watchlist_id: str, name: str = None, symbols=None):
        purchase = api.update_watchlist(self, watchlist_id: str, name: str = None, symbols=None)
  
#Implementation for data logger

#implementation for fethcing information for data logger

#implemenation for fetching market data about the symnol and logged data about the symbol

#trading strategy 