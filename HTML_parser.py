import requests




response = requests.get("https://qa06.happify.com/admin/")
print(response)

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        print("Encountered some data  :", data)

parser = MyHTMLParser()
parser.feed(response.text)

g = grab.Grab(html)
print(g.doc.select('//span[@class="card_info_inner"]').text())