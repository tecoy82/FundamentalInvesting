import time
from urllib.request import urlopen
import ssl
import utilities as util

ssl._create_default_https_context = ssl._create_unverified_context


def yahoo_key_stats(stock):
    try:
        source_code = urlopen('http://finance.yahoo.com/q/ks?s='+stock).read().decode("utf-8")
        price_book_ratio = source_code.split('Price/Book')[1].split('Fz(s) Fw(500) Ta(end)')[1].split('>')[1].split('<')[0]
        price_earnings_to_5yr_growth = source_code.split('PEG Ratio (5 yr expected)')[1].split('Fz(s) Fw(500) Ta(end)')[1].split('>')[1].split('<')[0]

        # print(type(price_book_ratio), price_book_ratio)
        if price_book_ratio != 'N/A' and price_book_ratio != '':
            if float(price_book_ratio) < 5:
                print("{} has a Price Book Ratio of {} and a Price/Earnings to 5yr Growth of {}".format(stock, price_book_ratio, price_earnings_to_5yr_growth))

    except Exception as e:
        print("Failed in the main loop", str(e))


def main():
    sp500short = ['a', 'aa', 'aapl', 'abbv', 'abc', 'abt', 'ace', 'aci', 'acn', 'act', 'adbe', 'adi', 'adm', 'adp']
    count = 0
    daily_sp500 = util.get_snp500()
    for sector, ticker in daily_sp500.items():
        for symbol in daily_sp500[sector]:
            if count > 15: break
            print("{}:{}".format(count,symbol))
            yahoo_key_stats(symbol)
            time.sleep(0.25)
            count += 1


if __name__ == "__main__":
    main()

