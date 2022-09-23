import requests
from bs4 import BeautifulSoup

with open("/home/mario/.config/i3/polybar/symbols.txt", "r") as symbols:
    SYMBOL = symbols.readline().strip("\n")


URL = 'https://finance.yahoo.com/quote/' + SYMBOL

page = requests.get(URL).text

soup = BeautifulSoup(page, 'html.parser')


quote = soup.find(
    attrs={"data-field": "regularMarketPrice", "data-symbol": SYMBOL}).text

direction = float(soup.find(
    attrs={"data-field": "regularMarketChange", "data-symbol": SYMBOL}).text) > 0

output = (str('%{F#f00}' + " " + quote + '%{F-} ' + SYMBOL),
          str('%{F#98c379}' + " " + quote + '%{F-} ' + SYMBOL))[direction]


print(output)
# print('%{F#f00}', " ", quote, '%{F-}', SYMBOL)
