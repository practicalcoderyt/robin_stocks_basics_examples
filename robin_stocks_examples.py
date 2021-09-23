import robin_stocks.robinhood as rs
from pyotp import TOTP as otp

def pretty_print_dict(dict):
    print('dictionary = {')
    for key in dict:
        print('\t' + str(key) + ' : ' + str(dict[key]))
    print('}')


def login():
    username = 'YOUR_USERNAME_HERE'
    password = 'YOUR_PASSWORD_HERE'
    totp = otp(0000000000000).now() # replace 0 with your otp id
    # account -> settings -> security and privacy -> Two-factor authentication -> turn on
    # Click the option that you were not able to scan the QR code and copy and paste the id here

    rs.authentication.login(username, password, mfa_code=totp, store_session=False)


def view_profile():
    profile_basics = rs.account.build_user_profile()
    pretty_print_dict(profile_basics)
    buying_power = rs.profiles.load_account_profile('buying_power')
    print('Buying power = ' + buying_power)
    owned_stocks = rs.account.build_holdings()
    pretty_print_dict(owned_stocks['GME'])
    buying_power_float = float(buying_power)

def load_stock():
    stocks = rs.stocks.get_fundamentals(['GME', 'AMZN'])
    latest_price = rs.stocks.get_latest_price('GME')
    print(latest_price)

def buy_stock():
    rs.orders.order_buy_fractional_by_price('GME', 100)
    rs.orders.order_buy_fractional_by_quantity('GME', 25)

def sell_stock():
    rs.orders.order_sell_fractional_by_price('GME', 100)
    rs.orders.order_sell_fractional_by_quantity('GME', 25)

def cancel_orders():
    rs.orders.cancel_all_stock_orders()
