import time
from urllib.request import urlopen
import ssl
import utilities as util

ssl._create_default_https_context = ssl._create_unverified_context


def yahoo_key_stats(stock):
    try:
        source_code = urlopen('http://finance.yahoo.com/q/ks?s='+stock).read().decode("utf-8")
        left_pbr = '<span data-reactid="57">Price/Book</span><!-- react-text: 58 --> <!-- /react-text --><!-- react-text: 59 -->(mrq)<!-- /react-text --><sup aria-label="KS_HELP_SUP_undefined" data-reactid="60"></sup></td><td class="Fz(s) Fw(500) Ta(end)" data-reactid="61">'
        right_pbr = '</td></tr><tr data-reactid="62"><td data-reactid="63">'
        price_book_ratio = source_code.split(left_pbr)[1].split(right_pbr)[0]

        # print("{} has a Price Book Ratio of {}".format(stock, price_book_ratio))
        if float(price_book_ratio) < 5:
            print("{} has a Price Book Ratio of {}".format(stock, price_book_ratio))

    except Exception as e:
        print("Failed in the main loop", str(e))


def main():
    sp500short = ['a', 'aa', 'aapl', 'abbv', 'abc', 'abt', 'ace', 'aci', 'acn', 'act', 'adbe', 'adi', 'adm', 'adp']
    count = 0
    daily_sp500 = util.get_snp500()
    for sector, ticker in daily_sp500.items():
        for symbol in daily_sp500[sector]:
            if count > 12: break
            yahoo_key_stats(symbol)
            time.sleep(0.5)
            count += 1


if __name__ == "__main__":
    main()

