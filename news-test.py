from lxml import html
import requests
page = requests.get('http://www.bestcollegereviews.org/50-best-college-towns-am$
tree = html.fromstring(page.content)
buyers = tree.xpath('//h2/text()')



prices = tree.xpath('//span[@class="item-price"]/text()')
print ('Buyers: ', buyers)
print ('Prices: ', prices)