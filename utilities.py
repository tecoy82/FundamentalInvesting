import requests
from bs4 import BeautifulSoup


def get_snp500():
    site = "http://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = requests.get(site, headers=hdr)
    soup = BeautifulSoup(req.content, "html.parser")

    table = soup.find('table', {'class': 'wikitable sortable'})
    sector_tickers = dict()
    for row in table.findAll('tr'):
        col = row.findAll('td')
        if len(col) > 0:
            sector = str(col[3].string.strip()).lower().replace(' ', '_')
            ticker = str(col[0].string.strip())
            if sector not in sector_tickers:
                sector_tickers[sector] = list()
            sector_tickers[sector].append(ticker)
    return sector_tickers
