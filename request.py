import requests
from lxml import html

page = requests.get('http://google.com')
tree = html.fromstring(page.content)
print(tree)
